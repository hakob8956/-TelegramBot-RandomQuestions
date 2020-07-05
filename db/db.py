import sqlite3
from sqlite3 import Error


database = r"db/TRQ.db"


def init():#initilization table
    sql_exist_table = '''SELECT name FROM sqlite_master WHERE type='table' AND name=?;'''
    exist = select(sql_exist_table,'UserSession')
    if(len(exist) == 0):
        create_table_userSession()
    
    
def execute(sql,data):
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute(sql,data)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        close_connection(conn)
def select(sql,data):
    rows = None
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute(sql,data)
        rows = c.fetchall()
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        close_connection(conn)
    return rows


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    return conn


def create_table_userSession(conn):
    sql = '''CREATE TABLE UserSession (
                UserId INTEGER PRIMARY KEY,
                ListQuestion text not NULL
                );'''
    execute(sql)

def close_connection(conn):
    conn.close()



