import warnings
import requests
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")

warnings.filterwarnings("ignore")

from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj


sql = 'select id,text from texts;'

text = cur.execute(sql).fetchall()
nlp.add_pipe('spacytextblob')

for lexi in text:
     doc = nlp(lexi[1])
     print(lexi,doc._.polarity,len(lexi))
