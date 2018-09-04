import sqlite3


class CManageDB:
    def __init__(self):
        self.conn = sqlite3.connect("db_shanti.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('create table all_lots (id integer primary key autoincrement, '
                            'id_lot integer, vk_link text, title text, money text)')

        self.cursor.execute('create table history (id integer primary key autoincrement, '
                            'id_lot_table integer references all_lots (id), name text, '
                            'money2 text, datetime real)')

        self.conn.commit()

    def add_lot_row(self, lot):

        self.cursor.execute('insert into all_lots (id_lot, vk_link, title, money) '
                            'values (:id_lot, :vk_link, :title, :money)',
                            {"id_lot": lot['id_lot']}, {"vk_link": lot['vk_link']},
                            {"title": lot['title']}, {"money": lot['money']})
        self.conn.commit()

    def add_history_row(self):
        pass

    def get_id_lot(self, lot):
        self.cursor.execute('select id from all_lots where id_lot ?', lot['id_lot'])
        return self.cursor.fetchall()

    def get_lot(self):
        pass

    def get_history_lot(self):
        pass
