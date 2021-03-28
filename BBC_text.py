import requests
from bs4 import BeautifulSoup
import pandas as pd

def text_extraction(df):
    for link in list(x['Links']):
        if '/news/' in link:
            c =lo.open_link(link,'div','ssrcss-16rg7hm-ContainerWithSidebarWrapper e1jl38b40')
            print(link)
            try:
                print(c[0].text[:100])
            except:
                print('Not right class')
        elif '/sport/' in link:
            c = lo.open_link(link,'div','qa-story-body story-body gel-pica gel-10/12@m gel-7/8@l gs-u-ml0@l gs-u-pb++')
            print(link)
            try:
                print(c[0].text[:100])
            except:
                print('Not right class')


    print('\n')
