import sqlite3

conn = sqlite3.connect("db_shanti.db")
cursor = conn.cursor()


cursor.execute("drop table all_lots ")
cursor.execute("drop table history ")
conn.commit()