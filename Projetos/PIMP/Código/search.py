import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


def search(text):
    query = urllib.parse.quote(text)
    # The '&sp=EgIQAQ%253D%253D' is used to only search for videos.
    url = "https://www.youtube.com/results?search_query=" + query + '&sp=EgIQAQ%253D%253D'
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup.find(attrs={'class': 'yt-uix-tile-link'})['href'][9:]
