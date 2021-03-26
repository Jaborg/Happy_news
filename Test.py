from newspaper import Article

url = "https://www.bbc.co.uk/news/uk-scotland-56539696"

# download and parse article
article = Article(url)
article.download()
article.parse()

# print article text
print(article.images)
