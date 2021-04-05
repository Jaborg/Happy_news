import warnings
import requests
from db_utils import db_connect


warnings.filterwarnings("ignore", message="Could not import the lzma module.")


import link_gatherer as e
import BBC_text as bb

bbc_news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

x = bbc_news.dataframe_collection()
j = bb.text_extraction(x)


con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj

columns = ['Id','Link','Title']
x = x.reindex(columns=columns)
x.to_sql('links',if_exists = 'append',con = con)
