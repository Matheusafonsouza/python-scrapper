import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

website = BeautifulSoup(content, 'html.parser')

new = website.find('div', attrs={'class': 'feed-post-body'})

print(new.prettify())