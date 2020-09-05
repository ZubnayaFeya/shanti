# удаление лишних пробелов из полученых данных
def clean_product_price(self, raw):
    raw = raw.replace('\n', '')
    raw_str = raw.split('  ')
    for i in range(len(raw_str)):
        if '' in raw_str:
            raw_str.remove('')
    return raw_str[0].strip()  # , raw_str[1].replace('\xa0', ' ').strip()
