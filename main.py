from bs4 import BeautifulSoup
from requests import get

file = open('links.txt', 'a')

url = "https://www.pkt.pl/mapa-strony/firmy/a"

page = get(url)
bs = BeautifulSoup(page.content, 'html.parser')

links = []

for link in bs.find_all('a'):
    links.append(link.get('href'))
for link in links:
    if "pkt.pl" in link:
        print(link)
        file.write(link + "\n")

file.close()
