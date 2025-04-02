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