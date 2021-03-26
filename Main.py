import warnings
import requests

warnings.filterwarnings("ignore", message="Could not import the lzma module.")
import Explore as e
import link_opener as lo

news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

x,y = news.dataframe_collection()

print(x.head(10))
