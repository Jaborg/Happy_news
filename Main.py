import warnings

warnings.filterwarnings("ignore", message="Could not import the lzma module.")
import Explore as e

news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

news.soup_intialisation()
x,y = news.dataframe_collection()


print(x.Links.unique())
