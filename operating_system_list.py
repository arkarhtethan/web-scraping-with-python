from bs4 import BeautifulSoup

with open("index.html", 'r') as f:

    content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    for li in soup.find_all('li'):

        print(li.getText())
