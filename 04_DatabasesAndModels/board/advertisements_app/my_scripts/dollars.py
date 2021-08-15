from bs4 import BeautifulSoup
import requests


def in_dollars(num):
    text = requests.get('https://www.banki.ru/products/currency/usd/')
    soup = BeautifulSoup(text.text, features="html.parser")
    new_num = num / float(soup.find('div', {'class': 'currency-table__large-text'}).text.replace(',', '.'))
    return round(new_num, 2)


if __name__ == '__main__':
    in_dollars(100)
