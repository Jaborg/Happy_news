import warnings
import requests
warnings.filterwarnings("ignore", message="Could not import the lzma module.")
import pandas as pd

from app.scraping import text_extractor as te


def main_links(news : object , db : object) -> pd.DataFrame:
    main_links_ = news.dataframe_collection()
    main_links_.apply(lambda row : db.insert_sql('links',
                                                ('Id,News,Date,Title,Link')
                                                ,(row.Id,row.News,row.Date,row.Title,row.Link))
                                                , axis = 1)

    return main_links_

def extracted_texts(links : pd.DataFrame, focus : str, letter : str, class_ : str, db : object) -> pd.DataFrame:
    extracted_texts_ = te.text_extraction(links,focus,letter,class_)
    extracted_texts_.apply(lambda row : db.insert_sql('texts',
                                                     ('Id,Text'),(row.Id,row.Text))
                                                     ,axis=1)
    return extracted_texts_

def polarised_text(links : pd.DataFrame, pol : object , cur : object, db : object) -> pd.DataFrame:
    polarised_text_ = pol.polarity_table(links['Id'].to_list(),cur)
    polarised_text_.apply(lambda row : db.insert_sql('polarity',
                                                   ('Id,Polarity,Length')
                                                   ,(row.Id,row.Polarity,row.Length))
                                                   , axis = 1)
    return polarised_text_
