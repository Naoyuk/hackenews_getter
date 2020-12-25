import requests
from bs4 import BeautifulSoup
import re

url = 'https://news.ycombinator.com/'
res = requests.get(url)

soup = BeautifulSoup(res.content, "html.parser")
links = soup.find_all('a', class_='storylink')

for link in links:
    print('--------------------------------------------------------------------')
    print(link.contents[0])
    print(link.attrs['href'])