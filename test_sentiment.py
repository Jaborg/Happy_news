
import numpy as np
import pandas as pd
import os
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt



from db_utils import db_connect


con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj


def word_image_gen(cur : object, id : str):
    sql = "select news from texts t inner join links l on l.id = t.id where t.id =  '{}'".format(id)
    text = cur.execute(sql).fetchone()
    sql = '''select text
                from texts t
                    inner join links l on l.id = t.id
                    inner join polarity p on p.id = t.id
                where news = '{news}' and length > 0 '''.format(news='DailyMail')
    text = cur.execute(sql).fetchall()
    values = ','.join(str(v) for v in text)
    print(type(values))
    my_path = os.path.abspath(__file__)
    wordcloud = WordCloud().generate(values)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()



word_image_gen(cur,'c2c7e0952032421c9adc37b3567e1ebb')
