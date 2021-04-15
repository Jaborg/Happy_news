import warnings
import requests
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")

warnings.filterwarnings("ignore")

from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj


sql = 'select text from texts;'

x = cur.execute(sql).fetchall()

text = x[2][0]
nlp.add_pipe('spacytextblob')
doc = nlp(text)
do = 'I love you so much we are so great'
do = nlp(do)

print(do._.polarity)
