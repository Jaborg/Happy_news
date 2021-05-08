import requests
from bs4 import BeautifulSoup
import pandas as pd

from app.scraping import link_opener as lo


def text_transform(t : list) -> list:
    return ' '.join([tt.text for tt in t])

def text_extraction(df : pd.DataFrame, specify : str, class_ : str) -> pd.DataFrame:
    dg = pd.DataFrame(columns=['Id','Text'])
    news_errors = 0
    for link in list(df['Link']):
        if specify in link:
            try:
                c = lo.open_link(link,'div',class_)
                bf = pd.DataFrame(data=[(df['Id'][df.Link == link].values[0]
                                        ,text_transform(c))],columns=['Id','Text'])
                bf['Text'] = bf['Text'].str.replace(r"[\"\,]", '')
                dg = dg.append(bf)
            except:
                news_errors += 1

    print('No. of news erros: '+ str(news_errors))
    return dg
