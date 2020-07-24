import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine("postgres://wbzlyjxjuqkbka:0ca9d84986635163ca4b0a3dabad60228116de6aad4de286ef4dddd41ffced06@ec2-34-225-162-157.compute-1.amazonaws.com:5432/deomiru5a02udf")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f= open("books.csv")
    reader = csv.reader(f)

    for isbn, title, author, year in reader:
        #db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", 
         #   {"isbn":isbn, "title":title,"author":author, "year":year})

        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Book added with ISBN:{isbn} Title:{title} Author: {author} Year: {year}")
        db.commit()
        

if __name__ == "__main__":
    main()
