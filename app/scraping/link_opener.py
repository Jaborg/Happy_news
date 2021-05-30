import requests
from bs4 import BeautifulSoup

def open_link(link: str,letter: str ,class_:str) -> list:
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    links = soup.find_all(letter, class_=class_)
    return links
