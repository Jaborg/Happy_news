import warnings
import requests

warnings.filterwarnings("ignore", message="Could not import the lzma module.")


import Explore as e
import BBC_text as bb

bbc_news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

x,y = bbc_news.dataframe_collection()
j = bb.text_extraction(x)
print(j.head(10))
