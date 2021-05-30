from app.scraping import scraping_collect as sc
import app.scraping.link_gatherer as e
from db_utils import db_connect
import db_connection as db
from app.analysis import polarity_calc as pol



print(dailymail.dataframe_collection())
con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj

bbc_news = e.Newscraper('http://bbc.co.uk/news','a',
        'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor','BBC')

guard_news = e.Newscraper('https://www.theguardian.com/uk','a',
        'u-faux-block-link__overlay js-headline-text','Guardian')

dailymail_news = e.Newscraper('https://www.dailymail.co.uk/news/index.html','h2',
        'linkro-darkred','DailyMail')




#Scrape of links, extraction of text , polarity assesment , push to SQLite
def main_():

    bbc_links,guard_links = sc.main_links(bbc_news,db), sc.main_links(guard_news,db)

    bbc_text= sc.extracted_texts(bbc_links,'/news/',
                              'ssrcss-uf6wea-RichTextComponentWrapper e1xue1i84',db)

    guard_text = sc.extracted_texts(guard_links,''
                 ,'article-body-commercial-selector css-79elbk article-body-viewer-selector',db)

    bbc_pol,guard_pol = sc.polarised_text(bbc_links,pol,cur,db), sc.polarised_text(guard_links,pol,cur,db)
    con.close()

    print('Insertion complete')



#main_()
