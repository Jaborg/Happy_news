import requests
from bs4 import BeautifulSoup

def open_link(link,letter,class_):
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    links = soup.find_all(letter, class_=class_)
    return links



# #dinks = open_link('https://www.bbc.co.uk/news/world-latin-america-56693406','div','ssrcss-3z08n3-RichTextContainer e5tfeyi2')
#
# dinks = open_link('https://www.bbc.co.uk/news/world-latin-america-56693406','div','ssrcss-16rg7hm-ContainerWithSidebarWrapper e1jl38b40')
# #x = ' '.join([dink.text for dink in dinks])
#
#
#x = dinks[0].text
# print(x)
