import warnings
import requests
from db_utils import db_connect
import db_connection as db


warnings.filterwarnings("ignore", message="Could not import the lzma module.")


import link_gatherer as e
import BBC_text as bb
import Polarity as pol

bbc_news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

main_links = bbc_news.dataframe_collection()
extracted_texts = bb.text_extraction(main_links)
polarised_text = pol.polarity_table(main_links['Id'].to_list())


main_links.apply(lambda row : db.insert_sql('links',('Id,Date,Title,Link'),(row.Id,row.Date,row.Title,row.Link)), axis = 1)
extracted_texts.apply(lambda row : db.insert_sql('texts',('Id,Text'),(row.Id,row.Text)),axis=1)
