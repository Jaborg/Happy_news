import requests
from bs4 import BeautifulSoup
import pandas as pd

import link_opener as lo

def text_transform(t):
    return ' '.join([tt.text for tt in t])

def text_extraction(df):
    dg = pd.DataFrame(columns=['Id','Text'])
    news_errors,sports_errors = 0,0
    for link in list(df['Link']):
        if '/news/' in link:
            try:
                c = lo.open_link(link,'div','ssrcss-3z08n3-RichTextContainer e5tfeyi2')
                bf = pd.DataFrame(data=[(df['Id'][df.Link == link].values[0],text_transform(c))],columns=['Id','Text'])
                bf['Text'] = bf['Text'].str.replace(r"[\"\',]", '')
                dg = dg.append(bf)
            except:
                news_errors += 1
        elif '/sport/' in link:
            try:
                c = lo.open_link(link,'div','qa-story-body story-body gel-pica gel-10/12@m gel-7/8@l gs-u-ml0@l gs-u-pb++')
                bf = pd.DataFrame(data=[(df['Id'][df.Link == link].values[0],text_transform(c))],columns=['Id','Text'])
                bf['Text'] = bf['Text'].str.replace(r"[\"\',]", '')
                dg = dg.append(bf)
            except:
                sports_errors += 1

    print('No. of news erros: '+ str(news_errors))
    print('No. of sports erros: '+ str(sports_errors))
    return dg
