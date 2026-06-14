import pandas as pd


def show_report(saved_articles):
    df = pd.DataFrame(saved_articles)

    print("Total articles saved:", len(df))
    print("Most frequent source:", df["source"].value_counts().idxmax())
    print("\nArticles by country/topic:")
    print(df["source"].value_counts())

