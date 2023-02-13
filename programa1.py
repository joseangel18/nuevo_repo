from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import requests


def gettitle(url):

    try:
        html = requests.get(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html.text, 'html.parser')
        title = soup.find_all('h3', limit=6)
    except AttributeError as e:
        return None

    return title


title = gettitle("https://www.bbc.com/news/technology")
print("BBC News Tecnología")
for titulo in title:
    print(titulo.text.strip())

title = gettitle(
    "https://www.marca.com/futbol/primera-division/clasificacion.html?intcmp=MENUMIGA&s_kw=clasificacion")
print("BBC News Tecnología")
for titulo in title:
    print(titulo.text.strip())
