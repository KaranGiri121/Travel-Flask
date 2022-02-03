import sqlite3

conn=sqlite3.connect("database.db")
conn.row_factory=sqlite3.Row
cur=conn.cursor()

# conn.execute("CREATE TABLE Dhangadi (Date TEXT,Lower TEXT,Upper TEXT)")
# conn.execute("CREATE TABLE Nepalgunj (Date TEXT,Lower TEXT,Upper TEXT)")
# conn.execute("CREATE TABLE Butwal (Date TEXT,Lower TEXT,Upper TEXT)")
# conn.execute("CREATE TABLE DhangadiMaharashtra (Date TEXT,Lower TEXT,Upper TEXT)")
# conn.execute("CREATE TABLE NepalgunjMaharashtra (Date TEXT,Lower TEXT,Upper TEXT)")
# conn.execute("CREATE TABLE ButwalMaharashtra (Date TEXT,Lower TEXT,Upper TEXT)")
# conn.execute("CREATE TABLE DhangadiGujarat (Date TEXT,Lower TEXT,Upper TEXT)")
# conn.execute("CREATE TABLE NepalgunjGujarat (Date TEXT,Lower TEXT,Upper TEXT)")
# conn.execute("CREATE TABLE ButwalGujarat (Date TEXT,Lower TEXT,Upper TEXT)")


# conn.close()