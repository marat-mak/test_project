from bs4 import BeautifulSoup
import requests


base = 'https://www.python.org'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
ul = soup.find('ul', class_ = 'menu')
a = ul.find_all('a' )
for i in a:
    print(i.getText(), base + i.get('href'))