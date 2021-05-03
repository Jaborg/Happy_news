import warnings
import requests
warnings.filterwarnings("ignore", message="Could not import the lzma module.")
import pandas as pd



from db_utils import db_connect
import db_connection as db
import link_gatherer as e
import text_extractor as te
import polarity_calc as pol

bbc_news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

guard_news = e.Newscraper('https://www.theguardian.com/uk','a',
        'u-faux-block-link__overlay js-headline-text')

def main_links(news : object) -> pd.DataFrame:
    main_links_ = news.dataframe_collection()
    main_links_.apply(lambda row : db.insert_sql('links',
                                                ('Id,Date,Title,Link')
                                                ,(row.Id,row.Date,row.Title,row.Link))
                                                , axis = 1)

    return main_links_

def extracted_texts(links : pd.DataFrame, focus : str, class_ : str) -> pd.DataFrame:
    extracted_texts_ = te.text_extraction(links,focus,class_)
    extracted_texts_.apply(lambda row : db.insert_sql('texts',
                                                    ('Id,Text'),(row.Id,row.Text))
                                                    ,axis=1)
    return extracted_texts_

def polarised_text(links : pd.DataFrame) -> pd.DataFrame:
    polarised_text_ = pol.polarity_table(links['Id'].to_list())
    polarised_text_.apply(lambda row : db.insert_sql('polarity',
                                                   ('Id,Polarity,Length')
                                                   ,(row.Id,row.Polarity,row.Length))
                                                   , axis = 1)
    return polarised_text_


#Scrape of links, extraction of text , polarity assesment , push to SQLite
def main_():
    bbc_links,guard_links = main_links(bbc_news),main_links(guard_news)
    bbc_text= extracted_texts(bbc_links,'/news/',
                              'ssrcss-3z08n3-RichTextContainer e5tfeyi2')
    guard_text = extracted_texts(guard_links,''
                 ,'article-body-commercial-selector css-79elbk article-body-viewer-selector')
    bbc_pol,guard_pol = polarised_text(bbc_links),polarised_text(guard_links)
    print('Insertion complete')



main_()
