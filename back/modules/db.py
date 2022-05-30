import sqlite3
from genericpath import exists

def create_db():
    if( not exists( "back/database.db" ) ):
        conn = sqlite3.connect('back/database.db')

        f = open('back/sql_dump/schema.sql', 'r' ) 
        conn.executescript(f.read())

        f = open('back/sql_dump/dump.sql')
        conn.executescript(f.read())

        conn.commit()
        conn.close()

def get_db_connection():
    conn = sqlite3.connect('back/database.db')
    conn.row_factory = sqlite3.Row
    return conn