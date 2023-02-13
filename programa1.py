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
        title = soup.find('title')
    except AttributeError as e:
        return None

    return title


title = gettitle("https://www.bbc.com/news/technology")
print("BBC News Tecnología")
for titulo in title:
    print(titulo.text.strip())
