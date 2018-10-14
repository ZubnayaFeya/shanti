# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect("db_shanti.db")
cursor = conn.cursor()


cursor.execute("drop table all_lots ")  # удалить таблицу all_lots
cursor.execute("drop table history ")   # удалить таблицу history


conn.commit()
conn.close()
