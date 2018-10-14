# a = [{'id': 12}, {'id': 13}, {'id': 14}, {'id': 15}, {'id': 16}, {'id': 17}]
# b = [11, 12, 13, 14, 15]
# d = []
# s = 13
# print(d)
# '''
# if s in a:
#     print('ok')
# else:
#     print('no')
# '''
# for s, i in enumerate(b):
#     #d.append(i['id'])
#     print(s, i)

import db_api
from time import time


a = {'11510928160158': {
    'vk_link': 'https://vk.com/wall-11510928_160158',
    'id_lot': 11510928160158,
    'title': 'Складной нож Ganzo «G7211»',
    'money': 'Обычная цена: 1890 руб.',
    'name': 'Найк Бойцов',
    'money2': '980 руб.'}
    }
# for i in a.items():
#     print(i)
# '''
db = db_api.CManageDB()
db.create_tables()
db.add_lot_row(a['11510928160158'])
id_a_lot = db.get_id_lot(11510928160158)
print(id_a_lot[0][0])
print(time())
db.add_history_row(id_a_lot[0][0], a['11510928160158'], time())
# '''
