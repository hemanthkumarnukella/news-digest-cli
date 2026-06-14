from api import NewsClient
from storage import DigestManager
from analysis import show_report
country=input("enter your country in ISO 3166-1 alpha-2 format:")
news = NewsClient(country)
count = 1
for article in news.articles:
    print(count, article['title'], article['source'])
    count += 1

fav_num = int(input("enter your article number:"))
chosen = news.articles[fav_num - 1]
storage = DigestManager()
storage.save(chosen)

print("\nYour saved articles:")
saved = storage.load()
for article in saved:
    print(article['title'], article['source'])

show_report(saved)

