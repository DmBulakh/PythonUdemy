import requests
from bs4 import BeautifulSoup

r = requests.get("https://uk.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%87%D1%83%D0%BA_%D0%92%D1%96%D0%BA%D1%82%D0%BE%D1%80_%D0%92%D0%BE%D0%BB%D0%BE%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87")
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.findAll("li")
# print(type(c))
# print(c)
# print(soup)

for i in all:
    print(i.text)
