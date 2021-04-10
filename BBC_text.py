import requests
from bs4 import BeautifulSoup
import pandas as pd

import link_opener as lo


def text_extraction(df):
    dg = pd.DataFrame(columns=['Id','Text'])
    news_errors,sports_errors = 0,0
    for link in list(df['Link']):
        if '/news/' in link:
            try:
                c = lo.open_link(link,'div','ssrcss-16rg7hm-ContainerWithSidebarWrapper e1jl38b40')
                bf = pd.DataFrame(data=[(df['Id'][df.Link == link].values[0],c[0].text)],columns=['Id','Text'])
                bf['Text'] = bf['Text'].str.replace(r"[\"\',]", '')
                dg = dg.append(bf)
            except:
                news_errors += 1
        elif '/sport/' in link:
            try:
                c = lo.open_link(link,'div','qa-story-body story-body gel-pica gel-10/12@m gel-7/8@l gs-u-ml0@l gs-u-pb++')
                bf = pd.DataFrame(data=[(df['Id'][df.Link == link].values[0],c[0].text)],columns=['Id','Text'])
                bf['Text'] = bf['Text'].str.replace(r"[\"\',]", '')
                dg = dg.append(bf)
            except:
                sports_errors += 1

    print('No. of news erros: '+ str(news_errors))
    print('No. of sports erros: '+ str(sports_errors))
    return dg
