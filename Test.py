import warnings
import requests
import spacy

nlp = spacy.load("en_core_web_sm")

warnings.filterwarnings("ignore")

from db_utils import db_connect

con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj


sql = 'select text from texts;'

x = cur.execute(sql).fetchall()

text = x[2][0]
doc = nlp(text)

for token in doc:
    print (token)

print(doc)
