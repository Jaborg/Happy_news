import warnings
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


sia = SentimentIntensityAnalyzer()



warnings.filterwarnings("ignore")

def word_image_gen(cur : object, id ; str):
    sql = 'select t'


def polarity_table(ids : list  , cur : object) -> pd.DataFrame:
    sql = 'select id,text from texts where id in {ids};'.format(ids=tuple(ids))
    text = cur.execute(sql).fetchall()
    polarity = pd.DataFrame(columns=['Id','Polarity','Length'])
    for lexi in text:
         ss = sia.polarity_scores(lexi[1])
         length,pol,id = len(lexi[1]),ss['compound'],lexi[0]
         polarity_sub = pd.DataFrame(data=[(id,pol,length)],columns=['Id','Polarity','Length'])
         polarity = polarity.append(polarity_sub)
    word_image_gen(cur,polarity['Id'].iloc(0)[0])
    return polarity
