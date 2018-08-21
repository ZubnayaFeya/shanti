#! /usr/lib/python3
# -*- coding: utf-8 -*-

# import urllib.request  не подошёл так как не умеет работать с кирилическими url
import requests
from bs4 import BeautifulSoup
import re


URL = 'https://шанти-шанти.рф/shantisales/'

lots = []


def get_page(url):
    html_page = requests.get(url).text
    soup = BeautifulSoup(html_page, 'lxml')
    table_auction = soup.find('table')
    return table_auction


def new_lot(link, id_lot, product, base_price, buyer, current_price):
    lot = {}
    lot['link_vk'] = link  # https://vk.com/wall-12345678_123456
    lot['id'] = id_lot
    lot['title'] = product
    lot['money'] = base_price
    lot['name'] = buyer
    lot['money2'] = current_price
    return lot


def get_id(link):
    pattern = r'[0-9]+[\_][0-9]+'
    id = int(re.findall(pattern, link)[0])
    return id


def clean_product_price(raw):
    raw_str = raw.split('  ')
    for i in range(len(raw_str)):
        if '' in raw_str:
            raw_str.remove('')
    return raw_str[0].strip(), raw_str[1].replace('\xa0', ' ').strip()


def get_buyer_current_price(str_html_lot):
    buyer = str_html_lot[2].text.strip()
    current_price = str_html_lot[3].text.strip()
    return buyer, current_price


def parse(html_data):
    for html_lot in html_data.find_all('tr')[1:]:
        str_html_lot = html_lot.find_all('td')
        vk_link = html_lot.find_all('a')[0].get('href')  # https://vk.com/wall-12345678_123456
        id_lot = get_id(vk_link)
        raw_product_price = str_html_lot[1].text
        product, price = clean_product_price(raw_product_price)
        buyer, current_price = get_buyer_current_price(str_html_lot)
        lots.append(new_lot(vk_link, id_lot, product, price, buyer, current_price))
    print(lots)


def chek_new_lot():
    pass


# print('{} - {} - {} - {} - {}'.format(product['id'], product['title'], product['money'], product['name'], product['money2']))


def mainloop():
    page = get_page(URL)
    parse(page)


if __name__ == '__main__':
    mainloop()


'''
сделал благодаря 
https://www.youtube.com/watch?v=KPXPr-KS-qk&index=16&list=WL&t=0s
'''
