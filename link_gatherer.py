import requests
from bs4 import BeautifulSoup
import pandas as pd
import typing

import link_opener as lo



class Newscraper(object):
    def __init__(self, url,letter,class_):
        self.url = url
        self.letter = letter
        self.class_ = class_

    def soup_intialisation(self):
        link_list,title_list = [],[]
        links = lo.open_link(self.url,self.letter,self.class_)
        for link in links:
            if len(link.text) > 15:
                link_list.append(link.get('href'))
                title_list.append((link.text).strip())
        return link_list,title_list

    def dataframe_collection(self) :
        link_list,title_list =  Newscraper.soup_intialisation(self)
        df_keyword = pd.DataFrame(
                {'Link': link_list,
                 'Title': title_list})
        df_keyword['Title'] = df_keyword.Title.str.replace('\n' , '')
        df_keyword = df_keyword.drop_duplicates(['Title'], keep='first')
        df_keyword['Id'] = df_keyword['Link'].str[:-5]
        return(df_keyword)
