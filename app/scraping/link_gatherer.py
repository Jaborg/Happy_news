from datetime import date
from typing import List, Tuple
import uuid as ud
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

from app.scraping import link_opener as lo


class Newscraper(object):
    def __init__(self, url: str, letter: str, class_: str, tag : str) -> None:
        self.url = url
        self.letter = letter
        self.class_ = class_
        self.tag = tag
        self.link_addon = url[:re.search(r"uk",url).end()]

    def soup_intialisation(self) -> tuple([List[str], List[str]]):
        link_list,title_list = [],[]
        links = lo.open_link(self.url,self.letter,self.class_)
        for link in links:
            if self.letter == 'a':
                if len(link.text) > 15:
                    if link.get('href')[:4] != 'http':
                        link_list.append(self.link_addon + link.get('href'))
                    else:
                        link_list.append(link.get('href'))
                    title_list.append((link.text).strip())
            else:
                if len(link.a.text) > 15:
                    if link.a.get('href')[:4] != 'http':
                        link_list.append(self.link_addon + link.a.get('href'))
                    else:
                        link_list.append(link.a.get('href'))
                    title_list.append((link.a.text).strip())

        return link_list,title_list

    def dataframe_collection(self) -> pd.DataFrame :
        link_list,title_list =  Newscraper.soup_intialisation(self)
        df_keyword = pd.DataFrame(
                {'Link': link_list,
                 'Title': title_list,
                 'News': self.tag})
        df_keyword['Title'] = df_keyword.Title.str.replace(r"[\"\,]", '')
        df_keyword['Id'] = [str(ud.uuid4()).replace('-','') for _ in range(len(df_keyword.index))]
        df_keyword = df_keyword.drop_duplicates( ['Id'],keep='first')
        today = date.today()
        df_keyword['Date'] = today.strftime("%d/%m/%Y")
        df_keyword = df_keyword.reindex(columns = ['Id','News','Date','Title','Link'])
        return(df_keyword.astype(str))
