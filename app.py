import requests
from bs4 import BeautifulSoup

base_url = 'https://lista.mercadolivre.com.br/'
product = 'mi band 5'
url = base_url + product.replace(' ', '-')

response = requests.get(url)

website = BeautifulSoup(response.text, 'html.parser')

products = website.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for product in products:
    title = product.find('h2', attrs={'class': 'ui-search-item__title'})
    link = product.find('a', attrs={'class': 'ui-search-link'})
    
    price = product.find('span', attrs={'class': 'price-tag-fraction'})
    cents = product.find('span', attrs={'class': 'price-tag-cents'})
    currency = product.find('span', attrs={'class': 'price-tag-symbol'})

    parsed_price = f'{currency.text} {price.text}'

    if cents:
        parsed_price += f'.{cents.text}'
    else:
        parsed_price += '.00'

    print(title.text)
    print(link['href'])
    print(parsed_price)