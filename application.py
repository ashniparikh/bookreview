import os
import requests


from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://wbzlyjxjuqkbka:0ca9d84986635163ca4b0a3dabad60228116de6aad4de286ef4dddd41ffced06@ec2-34-225-162-157.compute-1.amazonaws.com:5432/deomiru5a02udf")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "xlfQUhgA3aDMrXndJd53gg", "isbns": "9781632168146"})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)
    
    return "Project 1: TODO"
