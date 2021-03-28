import pandas as pd
import warnings
import requests

warnings.filterwarnings("ignore")

df = pd.DataFrame(columns=['Link','Text'])

link = 'www.bbt.co.uk'
text= ' I hate this site'

dg = pd.DataFrame(data=[(link,text)],columns=['Link','Text'])
df = df.append(dg)


print(df.head())
