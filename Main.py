import warnings
import requests
from db_utils import db_connect
import db_connection as db


warnings.filterwarnings("ignore", message="Could not import the lzma module.")


import link_gatherer as e
import BBC_text as bb
import Polarity as pol

# bbc_news = e.Newscraper('http://bbc.co.uk','a',
#         'ssrcss-10ivm7i-PromoLink e1f5wbog5')

guard_news = e.Newscraper('https://www.theguardian.com/uk','a',
        'u-faux-block-link__overlay js-headline-text')

main_links = guard_news.dataframe_collection()
print(main_links.Link)


# main_links = bbc_news.dataframe_collection()
# main_links.apply(lambda row : db.insert_sql('links',('Id,Date,Title,Link'),(row.Id,row.Date,row.Title,row.Link)), axis = 1)
#
# extracted_texts = bb.text_extraction(main_links)
# extracted_texts.apply(lambda row : db.insert_sql('texts',('Id,Text'),(row.Id,row.Text)),axis=1)
#
# polarised_text = pol.polarity_table(main_links['Id'].to_list())
# polarised_text.apply(lambda row : db.insert_sql('polarity',('Id,Polarity,Length'),(row.Id,row.Polarity,row.Length)), axis = 1)
