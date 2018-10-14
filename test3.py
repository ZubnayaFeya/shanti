# -*- coding: utf-8 -*-

import sqlite3
from time import time
from testing_data import *


def add_lot_row(lot):
    cursor.execute('insert into all_lots(id_lot, vk_link, title, money, flag) '
                   'select :id_lot, :vk_link, :title, :money, :flag where not exists '
                   '(select 1 from all_lots where id_lot = :id_lot)',
                   {"id_lot": lot['id'], "vk_link": lot['link_vk'],
                    "title": lot['title'], "money": lot['money'],
                    "flag": 1})
    conn.commit()


def get_id_lot(vk_id_lot):
    cursor.execute('select id from all_lots where id_lot = ?', (vk_id_lot, ))
    return cursor.fetchall()


def add_history_row(lot, datetime):
    cursor.execute('insert into history (id_lot_table, name, money2, datetime) '
                   'values (:id_lot, :name, :money2, :datetime)',
                   {"id_lot": lot['id'], "name": lot['name'],
                   "money2": lot['money2'], "datetime": datetime})
    conn.commit()


conn = sqlite3.connect("db_shanti.db")
cursor = conn.cursor()

cursor.execute('create table if not exists all_lots ('
               'id_lot integer primary key unique, vk_link text,'
               ' title text, money text, flag integer)')

cursor.execute('create table if not exists history ('
               'id_lot_table integer references all_lots (id_lot), '
               'name text, money2 text, datetime real)')
conn.commit()


add_lot_row(a['11510928160158'])
add_lot_row(b['11510928179946'])
add_lot_row(c['11510928179799'])
print(time())
add_history_row(a['11510928160158'], time())
add_history_row(b['11510928179946'], time())
add_history_row(c['11510928179799'], time())

conn.commit()
cursor.close()



