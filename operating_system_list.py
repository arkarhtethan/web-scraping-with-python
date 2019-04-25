from bs4 import BeautifulSoup

with open("index.html", 'r') as f:

    content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    body = soup.body

    for ele in body.descendants:

        print(ele)

    # for ele in soup.body.recursiveChildGenerator():
    #
    #     if not ele.name is None:
    #
    #         print(ele.name)

    # for li in soup.find_all('li'):
    #
    #     print(li.getText())

    # print(ul)
