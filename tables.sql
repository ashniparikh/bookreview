CREATE TABLE users(
    userid SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE books (
    bookid SERIAL PRIMARY KEY,
    isbn VARCHAR UNIQUE NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year SMALLINT NOT NULL
);

CREATE TABLE reviews (
    reviewid SERIAL PRIMARY KEY,
    rating INTEGER NOT NULL CONSTRAINT Invalid_Rating CHECK (rating <=5 AND rating>=1),
    review VARCHAR,
    user_id INTEGER REFERENCES users,
    book_id INTEGER REFERENCES books,
);