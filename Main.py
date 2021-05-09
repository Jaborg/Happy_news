from app.scraping import scraping_collect as sc
import app.scraping.link_gatherer as e
from db_utils import db_connect
import db_connection as db
from app.analysis import polarity_calc as pol



con = db_connect()  # connect to the database
cur = con.cursor() # instantiate a cursor obj

bbc_news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5','BBC')

guard_news = e.Newscraper('https://www.theguardian.com/uk','a',
        'u-faux-block-link__overlay js-headline-text','Guardian')



#Scrape of links, extraction of text , polarity assesment , push to SQLite
def main_():

    bbc_links,guard_links = sc.main_links(bbc_news,db), sc.main_links(guard_news,db)

    bbc_text= sc.extracted_texts(bbc_links,'/news/',
                              'ssrcss-3z08n3-RichTextContainer e5tfeyi2',db)

    guard_text = sc.extracted_texts(guard_links,''
                 ,'article-body-commercial-selector css-79elbk article-body-viewer-selector',db)

    bbc_pol,guard_pol = sc.polarised_text(bbc_links,pol,cur,db), sc.polarised_text(guard_links,pol,cur,db)
    con.close()

    print('Insertion complete')



main_()
