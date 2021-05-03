import scraping_collect as sc
import link_gatherer as e

bbc_news = e.Newscraper('http://bbc.co.uk','a',
        'ssrcss-10ivm7i-PromoLink e1f5wbog5')

guard_news = e.Newscraper('https://www.theguardian.com/uk','a',
        'u-faux-block-link__overlay js-headline-text')



#Scrape of links, extraction of text , polarity assesment , push to SQLite
def main_():
    bbc_links,guard_links = sc.main_links(bbc_news),main_links(guard_news)
    bbc_text= sc.extracted_texts(bbc_links,'/news/',
                              'ssrcss-3z08n3-RichTextContainer e5tfeyi2')
    guard_text = sc.extracted_texts(guard_links,''
                 ,'article-body-commercial-selector css-79elbk article-body-viewer-selector')
    bbc_pol,guard_pol = polarised_text(bbc_links),polarised_text(guard_links)
    print('Insertion complete')



main_()
