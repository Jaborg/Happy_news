import warnings
import requests

warnings.filterwarnings("ignore", message="Could not import the lzma module.")
import Explore as e
import link_opener as lo

bbc_news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

x,y = bbc_news.dataframe_collection()
