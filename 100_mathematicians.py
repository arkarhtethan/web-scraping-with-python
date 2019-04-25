import requests
from bs4 import BeautifulSoup

url = "http://www.fabpedigree.com/james/mathmen.htm"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

names = set()

for li in soup.select('li'):

    for name in li.text.split("\n"):

        if len(name) > 0:

            names.add(name)

for i, name in enumerate(names):

    print(i, name)
