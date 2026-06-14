import requests
class NewsClient():
    def __init__(self,country):
        try:
            response=requests.get(url=f"https://newsapi.org/v2/top-headlines?country={country}&"
                                       f"apiKey=58da76bd1490405e9e50d456bc135ced")
            full_news=response.json()
            self.articles = [{
                "title": article["title"],
                    "source": article["source"]["name"],
                "url": article["url"],
                "date": article["publishedAt"]
                } for article in full_news["articles"]]


        except requests.exceptions.ConnectionError:
            print("No internet connection.")
            self.articles = []








