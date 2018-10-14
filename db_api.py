import sqlite3


class CManageDB:
    def __init__(self):
        self.conn = sqlite3.connect("db_shanti.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('create table if not exists all_lots (id integer primary key autoincrement, '
                            'id_lot integer unique, vk_link text, title text, money text, flag integer)')

        self.cursor.execute('create table if not exists history (id integer primary key autoincrement, '
                            'id_lot_table integer references all_lots (id), name text, '
                            'money2 text, datetime real)')

        self.conn.commit()

    def add_lot_row(self, lot):

        self.cursor.execute('insert or ignore into all_lots (id_lot, vk_link, title, money) '
                            'values (:id_lot, :vk_link, :title, :money)',
                            {"id_lot": lot['id_lot'], "vk_link": lot['vk_link'],
                             "title": lot['title'], "money": lot['money']})
        self.conn.commit()

    def add_history_row(self, id_lot, lot, datetime):
        self.cursor.execute('insert into history (id_lot_table, name, money2, datetime) '
                            'values (:id_lot, :name, :money2, :datetime)',
                            {"id_lot": id_lot, "name": lot['name'],
                            "money2": lot['money2'], "datetime": datetime})
        self.conn.commit()

    def get_id_lot(self, vk_id_lot):
        self.cursor.execute('select id from all_lots where id_lot = ?', (vk_id_lot, ))
        return self.cursor.fetchall()

    def get_lot(self):
        pass

    def get_history_lot(self):
        pass
