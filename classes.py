#! /usr/lib/python3
# -*- coding: utf-8 -*-

# import urllib.request  не подошёл так как не умеет работать с кирилическими url
import requests
from bs4 import BeautifulSoup
import re
import time

import config


class CParser:
    def __init__(self):
        self.full_lots = []
        self.id_full_lots = []
        self.lots = []
        self.url = config.URL

    def get_page(self):
        html_page = requests.get(self.url).text
        soup = BeautifulSoup(html_page, 'lxml')
        table_auction = soup.find('table')
        return table_auction

    def new_lot(self, link, id_lot, product, base_price, buyer, current_price):
        lot = {}
        lot['link_vk'] = link  # https://vk.com/wall-12345678_123456
        lot['id'] = id_lot
        lot['title'] = product
        lot['money'] = base_price
        lot['name'] = buyer
        lot['money2'] = current_price
        return lot

    def get_id(self, link):
        pattern = r'[0-9]+[\_][0-9]+'
        id = int(re.findall(pattern, link)[0])
        return str(id)

    def clean_product_price(self, raw):
        raw_str = raw.split('  ')
        for i in range(len(raw_str)):
            if '' in raw_str:
                raw_str.remove('')
        return raw_str[0].strip(), raw_str[1].replace('\xa0', ' ').strip()

    def get_buyer_current_price(self, str_html_lot):
        buyer = str_html_lot[2].text.strip()
        current_price = str_html_lot[3].text.strip()
        return buyer, current_price

    def parse(self, html_data):
        for html_lot in html_data.find_all('tr')[1:]:
            str_html_lot = html_lot.find_all('td')
            vk_link = html_lot.find_all('a')[0].get('href')  # https://vk.com/wall-12345678_123456
            id_lot = self.get_id(vk_link)
            raw_product_price = str_html_lot[1].text
            product, price = self.clean_product_price(raw_product_price)
            buyer, current_price = self.get_buyer_current_price(str_html_lot)
            self.lots.append(self.new_lot(vk_link, id_lot, product, price, buyer, current_price))
            self.id_full_lots.append(id_lot)

    def print_lots(self):
        for lot in self.lots:
            self.add_print_lot(lot)
            # print('всего {} лотов'.format(len(self.full_lots)))
        self.lots.clear()

    def check_new_lots(self):
        for lot in self.lots:
            if lot['id'] not in self.id_full_lots:
                self.add_print_lot(lot)
                print('всего {} лотов'.format(len(self.full_lots)))

    def check_sold_lot(self):
        id_lots = []
        for lot in self.lots:
            id_lots.append(lot['id'])
        for id in self.id_full_lots:
            if id not in id_lots:
                self.del_lot(id)
        id_lots.clear()

    def del_lot(self, id):
        for lot in self.full_lots:
            if lot['id'] == id:
                self.full_lots.remove(lot)
                self.id_full_lots.remove(id)
                print('всего {} лотов'.format(len(self.full_lots)))

    def add_print_lot(self, lot):
        self.id_full_lots.append(lot['id'])
        self.full_lots.append(lot)
        print('{} - {} - {} - {} - {}'.format(lot['id'], lot['title'], lot['money'], lot['name'], lot['money2']))

    def mainloop(self):
        page = self.get_page()
        self.parse(page)
        self.print_lots()
        print('всего {} лотов'.format(len(self.full_lots)))
        while True:
            time.sleep(600)
            page = self.get_page()
            self.parse(page)
            self.check_new_lots()
            self.check_sold_lot()
            self.lots.clear()


if __name__ == '__main__':
    pars = CParser()
    pars.mainloop()


'''
сделал благодаря 
https://www.youtube.com/watch?v=KPXPr-KS-qk&index=16&list=WL&t=0s
'''
