import requests
from bs4 import BeautifulSoup
import pandas as pd

news_list = []

response = requests.get('https://g1.globo.com/')

content = response.content

website = BeautifulSoup(content, 'html.parser')

news = website.findAll('div', attrs={'class': 'feed-post-body'})

for new in news:
    title = new.find('a', attrs={'class': 'feed-post-link'})
    subtitle = new.find('div', attrs={'class': 'feed-post-body-resumo'})

    if subtitle:
        news_list.append([title.text, subtitle.text, title['href']])
    else:
        news_list.append([title.text, '', title['href']])

news = pd.DataFrame(news_list, columns=['Title', 'Subtitle', 'Link'])
news.to_csv('news.csv', index=False)
