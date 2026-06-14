import csv
class DigestManager:
    def __init__(self):
        self.filename="favourites.csv"


    def save(self, article):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                saved_urls = [row["url"] for row in reader]
        except FileNotFoundError:
            saved_urls = []

        if article["url"] not in saved_urls:
            with open(self.filename, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["title", "source", "url", "date"])
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(article)
            print("Saved!")
        else:
            print("Already saved!")

    def load(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []

