import sqlite3
from time import time


def add_lot_row(lot):
    cursor.execute('insert into all_lots(id_lot, vk_link, title, money) '
                   'select :id_lot, :vk_link, :title, :money '
                   'where not exists '
                   '(select 1from all_lots where id_lot = :id_lot)',
                   {"id_lot": lot['id_lot'], "vk_link": lot['vk_link'],
                    "title": lot['title'], "money": lot['money']})

    # cursor.execute('insert into all_lots (id_lot, vk_link, title, money) '
    #                'select :id_lot, :vk_link, :title, :money'
    #                'except select id_lot, vk_link, title, money from all_lots where id_lot = :id lot',
    #                {"id_lot": lot['id_lot'], "vk_link": lot['vk_link'],
    #                 "title": lot['title'], "money": lot['money']})
    conn.commit()


def get_id_lot(vk_id_lot):
    cursor.execute('select id from all_lots where id_lot = ?', (vk_id_lot, ))
    return cursor.fetchall()


def add_history_row(id_lot, lot, datetime):
    cursor.execute('insert into history (id_lot_table, name, money2, datetime) '
                   'values (:id_lot, :name, :money2, :datetime)',
                   {"id_lot": id_lot, "name": lot['name'],
                   "money2": lot['money2'], "datetime": datetime})


a = {'11510928160158': {
    'vk_link': 'https://vk.com/wall-11510928_160158',
    'id_lot': 11510928160158,
    'title': 'Складной нож Ganzo «G7211»',
    'money': 'Обычная цена: 1890 руб.',
    'name': 'Найк Бойцов',
    'money2': '980 руб.'}
    }
conn = sqlite3.connect("db_shanti.db")
cursor = conn.cursor()

cursor.execute('create table if not exists all_lots (id integer primary key autoincrement, '
               'id_lot integer unique, vk_link text, title text, money text, flag integer)')

cursor.execute('create table if not exists history (id integer primary key autoincrement, '
               'id_lot_table integer references all_lots (id), name text, '
               'money2 text, datetime real)')
conn.commit()

add_lot_row(a['11510928160158'])
id_a_lot = get_id_lot(11510928160158)
print(id_a_lot[0][0])
print(time())
add_history_row(id_a_lot[0][0], a['11510928160158'], time())

conn.commit()
cursor.close()



