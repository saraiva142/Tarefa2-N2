import sqlite3
conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute(
 '''CREATE TABLE ALUNOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    NOME          TEXT    NOT NULL,
    N1            REAL,
    N2            REAL,
    MEDIA         REAL);'''
)
print ("Table created successfully");

conn.close()