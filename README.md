# Book Reviews
My solution for Project 1 for CS50's Web Programming with Python and JavaScript

# Overview
The goal of the project is to build a book review website. There will be a user system(to login and register). On the page, the user can search for books, leave a review, and see reviews made by other users. Also, there is an integration with the API provided by Goodreads to show extra information about the books.In addition, users are able to query for book details and book reviews programmatically via website's API.

# Getting Started

# Pre-requisites
Make sure you have the following installed on your machine:

postgreSQL
Python 3.7.2

# Installation
1. Clone the repository
2. In your terminal window, navigate into the project
3. Run pip3 install -r requirements.txt in your terminal window to make sure that all of the necessary Python packages       (Flask and SQLAlchemy, for instance) are installed.
4. Set the environment variables:
    export FLASK_APP=application.py. On Windows, the command is instead set FLASK_APP=application.py
    You may optionally want to set the environment variable FLASK_DEBUG to 1, which will activate Flask’s debugger and will automatically reload your web application whenever you save a change to a file.
5. Set up an PostgresSQL Database(you can get one for free in Heroku), for this project you cand use any SQL database.       And take note of the URI, you will need it.
   $ export DATABASE_URL=<YOUR-URL>
6. Set up an developer account on Goodreads and take note of your api key; KEY = is your API key, will give you the          review and rating data for the book with the provided ISBN number (register at goodreads.com)
7. Run python3 import.py to import a spreadsheet in CSV format of 5000 different books to your database
8. Finally execute flask run command in your terminal to start the server
   Let's open a browers a go to http://localhost:5000 to start usin the app.

# API Access
If users make a GET request to the website’s /api/<isbn> route, where <isbn> is an ISBN number, the website returns a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. Example format:

{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}
