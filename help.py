import sqlite3 as sql

conn=sql.connect("database.db")

conn.row_factory=sql.Row

cur=conn.cursor()

Place="Dhangadi"
Date='2022-02-26'
cur.execute(f"SELECT * FROM {Place}")
x=cur.fetchall()


def delete(x):
    for i in x:
        cur.execute(f"DELETE FROM Dhangadi WHERE Date='{i['Date']}'")

    conn.commit()