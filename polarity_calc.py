import warnings
import requests
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')
warnings.filterwarnings("ignore")

from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj


def polarity_table(ids : list) -> pd.DataFrame:
    sql = 'select id,text from texts where id in {ids};'.format(ids=tuple(ids))
    text = cur.execute(sql).fetchall()
    print(text)
    polarity = pd.DataFrame(columns=['Id','Polarity','Length'])
    for lexi in text:
         doc = nlp(lexi[1])
         length,pol,id = len([token.text for token in doc]),doc._.polarity,lexi[0]
         polarity_sub = pd.DataFrame(data=[(id,pol,length)],columns=['Id','Polarity','Length'])
         polarity = polarity.append(polarity_sub)
    return polarity
