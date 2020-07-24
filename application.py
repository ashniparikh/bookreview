import os


from flask import Flask, session, render_template, redirect, request, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)




# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://wbzlyjxjuqkbka:0ca9d84986635163ca4b0a3dabad60228116de6aad4de286ef4dddd41ffced06@ec2-34-225-162-157.compute-1.amazonaws.com:5432/deomiru5a02udf")
db = scoped_session(sessionmaker(bind=engine))

## Helper
def login_required(f):
    """
    Decorate routes to require login.

    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("email") is None:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    #if method is GET, show the registration form

    if request.method == "GET":
        return render_template("register.html")

    #if method is POST:

    else:
        #if form values are empty show error

        if not request.form.get("user_name"):
            return render_template("error.html",message="Must provide User Name")
        elif not request.form.get("email"):
            return render_template("error.html",message="Must provide Email")
        elif not request.form.get("password1") or not request.form.get("password2"):
            return render_template("error.html",message="Must provide Password")
        elif request.form.get("password1") != request.form.get("password2"):
            return render_template("error.html",message="Password does not match")

        else:
            #assign values to variables
            username=request.form.get("user_name")
            print(username)
            email =request.form.get("email")
            print(email)
            password=request.form.get("password1")
            print(password)

            register1=db.execute("SELECT * FROM users WHERE email LIKE :email",{"email":email}).fetchone()

            if register1:
                return render_template("error.html",message="EmailId is already in use")

            #try to commit to database and raise error if any

            try:
                register=db.execute("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)",
                    {"username": username, "email": email, "password": generate_password_hash(password)})
                print(register)
            except Exception as e :
                return render_template("error.html",message=e)

            db.commit()
            print(db.commit())
            return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():

    # forget any userid
    session.clear()

    if request.method == "POST" :
        form_email=request.form.get("email")
        form_password=request.form.get("password")

        #if form values are empty show error
        
        if not form_email:
            return render_template("error.html", message="Must provide email")
        elif not form_password:
            return render_template("error.html", message="Must provide password")
        
        # check into database for email and password
        user= db.execute("SELECT * FROM users WHERE email LIKE :email", {"email":form_email}).fetchone()

        # check if user exists or not
        if user is None:
            return render_template("error.html",message="User doesn't exist")
        # check password is valid or not
        if not check_password_hash(user.password,form_password):
            return render_template("error.html",message="Invalid password")

        # Remember which user has logged in
        session["user_id"]=user.userid
        session["username"]=user.username
        session["email"]=user.email
        session["logged_in"]=True

        return redirect(url_for("search"))
    # User reached route via GET Method
    else:
        return render_template("login.html")

@app.route("/search", methods=["GET","POST"])
@login_required
def search():

    if request.method == "GET":    
        return render_template("search.html")
    
    else:
        search_field=request.form.get("input-search")

        if search_field is None:
            return render_template("error.html",message="Search field can not be empty")
        try:
            result = db.execute("SELECT * FROM books WHERE LOWER(isbn) LIKE :search_field OR LOWER(title) LIKE :search_field OR LOWER(author) LIKE :search_field", {"search_field": "%" + search_field.lower() + "%"}).fetchall()
            print(result)
        except Exception as e:
            return render_template("error.html", message=e)
        if not result:
            return render_template("error.html", message="Your search did not match any documents")
        return render_template("list.html", result=result)

