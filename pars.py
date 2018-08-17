#! /usr/lib/python3
# -*- coding: utf-8 -*-

import urllib.request
import requests
from bs4 import BeautifulSoup
import re


url = 'https://шанти-шанти.рф/shantisales/'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', class_='table table-striped')

    products = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        link = row.find_all('a')[0].get('href')
        pattern = r'[0-9]+[\_][0-9]+'
        id = int(re.findall(pattern, link)[0])
        a = cols[1].text

        prod = a.split('  ')
        for i in range(len(prod)):
            if '' in prod:
                prod.remove('')

        products.append({
            'link_vk': link,  # https://vk.com/wall-12345678_123456
            'id': id,
            'title': prod[0].strip(),
            'money': prod[1].replace('\xa0', ' ').strip(),
            'name': cols[2].text.strip(),
            'money2': cols[3].text.strip()
        })

    for product in products:
        print('{} - {} - {} - {} - {}'.format(product['id'], product['title'], product['money'], product['name'], product['money2']))
    print(len(products))

def main():
    # parse(get_html('https://shanti-shanti.com/shantisales'))
    page = requests.get(url)
    parse(page.text)


if __name__ == '__main__':
    main()


'''
сделал благодаря 
https://www.youtube.com/watch?v=KPXPr-KS-qk&index=16&list=WL&t=0s
'''
