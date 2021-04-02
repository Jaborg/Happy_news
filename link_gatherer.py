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
        link_list,text_list = [],[]
        links = lo.open_link(self.url,self.letter,self.class_)
        for link in links:
            if len(link.text) > 15:
                link_list.append(link.get('href'))
                text_list.append((link.text).strip())
        return link_list,text_list

    def dataframe_collection(self) :
        link_list,text_list =  Newscraper.soup_intialisation(self)
        df_keyword = pd.DataFrame(
                {'Links': link_list,
                 'Text': text_list})
        df_keyword['Text'] = df_keyword.Text.str.replace('\n' , '')
        df_keyword = df_keyword.drop_duplicates(['Text'], keep='first')
        return(df_keyword)
