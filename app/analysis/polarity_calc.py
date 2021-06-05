import warnings
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
import pandas as pd

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')


warnings.filterwarnings("ignore")




def polarity_table(ids : list  , cur : object) -> pd.DataFrame:
    sql = 'select id,text from texts where id in {ids};'.format(ids=tuple(ids))
    text = cur.execute(sql).fetchall()
    polarity = pd.DataFrame(columns=['Id','Polarity','Length'])
    for lexi in text:
         ss = sia.polarity_scores(lexi[1])
         length,pol,id = len(lexi[1]),ss['compound'],lexi[0]
         polarity_sub = pd.DataFrame(data=[(id,pol,length)],columns=['Id','Polarity','Length'])
         polarity = polarity.append(polarity_sub)
    return polarity
