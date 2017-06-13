#! python3

import sqlite3
import json

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Create some tables
cur.executescript('''
DROP TABLE IF EXISTS USer;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE,
    email  TEXT
);

CREATE TABLE Course (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member(
    user_id    INTEGER,
    course_id    INTEGER,
    role    INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')


fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'roster_data.json'
