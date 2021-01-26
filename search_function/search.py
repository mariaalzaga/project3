import pandas as pd
import numpy as np
import time

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("netflix_titles.csv")

df = df.iloc[20:].reset_index(drop=True)

df["date_added"] = pd.to_datetime(df['date_added'])
df['year'] = df['date_added'].dt.year
df['month'] = df['date_added'].dt.month
df['day'] = df['date_added'].dt.day

search_df = df.drop(["show_id", "duration", "year", "month", "day"], axis=1)
titles_df = search_df.drop(["type", "director","cast","country","release_year","listed_in", "description"], axis=1)

test = search_df["title"].values

cv = make_pipeline(
    CountVectorizer(
        ngram_range=(3, 3),
        analyzer="char_wb",
    ),
    Normalizer()
)

cv = cv.fit(test)

X = cv.transform(test)

movie_title = input("\nSearch for Movie: \n")

def search(term):
    
    X_term = cv.transform([term])
    simular = cosine_similarity(X_term, X)
    
    final_list = []
    
    idxmax = np.argmax(simular[0])
           
    sim_scores = list(enumerate(simular[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:5]
    movie_indices = [i[0] for i in sim_scores]
    
    return titles_df.iloc[movie_indices].reset_index(drop=True)

print(f"\nSearching movie: {movie_title}\n")
print("\nMovies on Netflix\n")
print((search(movie_title)).to_markdown())