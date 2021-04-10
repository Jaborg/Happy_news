import warnings
import requests
from db_utils import db_connect
import db_connection as db


warnings.filterwarnings("ignore", message="Could not import the lzma module.")


import link_gatherer as e
import BBC_text as bb

bbc_news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

x = bbc_news.dataframe_collection()
j = bb.text_extraction(x)



x.apply(lambda row : db.insert_sql('links',('Id,Date,Title,Link'),(row.Id,row.Date,row.Title,row.Link)), axis = 1)
j.apply(lambda row : db.insert_sql('texts',('Id,Text'),(row.Id,row.Text)),axis=1)
# x.to_sql('links',if_exists = 'append',con = con,index=False, index_label='Id')
# j.to_sql('texts',if_exists = 'append',con = con,index=False, index_label='Id')

# use the generic Exception, both IntegrityError and sqlite3.IntegrityError caused trouble.
