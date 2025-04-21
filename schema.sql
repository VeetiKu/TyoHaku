CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
    
);
CREATE TABLE items (
    id INTEGER PRIMARY KEY ,
    title TEXT ,
    author TEXT,
    description TEXT ,
    salary INTEGER ,
    location TEXT ,
    deadline DATE,
    user_id INTEGER REFERENCES users
);

CREATE TABLE classes (
     id INTEGER PRIMARY KEY,
     title TEXT,
     value TEXT
 );

CREATE TABLE item_classes (
    id INTEGER PRIMARY KEY,
    item_id INTEGER REFERENCES items ON DELETE CASCADE,
    title TEXT,
    value TEXT
);

CREATE TABLE applications (
     id INTEGER PRIMARY KEY,
     item_id INTEGER REFERENCES items ON DELETE CASCADE,
     user_id INTEGER REFERENCES users,
     message TEXT
 );