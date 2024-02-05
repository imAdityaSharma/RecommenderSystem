import ast
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle



def str_to_list(text):
    l0 = []
    for i in ast.literal_eval(text):
        l0.append(i['name'])
    return l0
def castcon3(text):
    l3 = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            l3.append(i['name'])
        counter += 1
    return l3


def director(text):
    l2 = []
    for i in ast.literal_eval(text):
        if i['job'] == 'director':
            l2.append(i['name'])
    return l2

def collapse(t):
    l1 = []
    for i in t:
        l1.append(i.replace(" ", ""))
    return l1


def generate_similarity():
    df_movie = pd.read_csv('tmdb_5000_movies.csv', header=0)
    df_credtis = pd.read_csv('tmdb_5000_credits.csv', header=0)
    # df_credtis
    movies = df_movie.merge(df_credtis, on='title')
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
    movies.dropna(inplace=True)
    movies['genres'] = movies['genres'].apply(str_to_list)
    movies['keywords'] = movies['keywords'].apply(str_to_list)
    movies['cast'] = movies['cast'].apply(castcon3)
    movies['crew'] = movies['crew'].apply(director)
    # movies.sample(5)
    movies['cast'] = movies['cast'].apply(collapse)
    movies['crew'] = movies['crew'].apply(collapse)
    movies['genres'] = movies['genres'].apply(collapse)
    movies['keywords'] = movies['keywords'].apply(collapse)
    movies['overview'] = movies['overview'].apply(lambda x: x.split())
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
    new = movies.drop(columns=['overview', 'genres', 'keywords', 'cast', 'crew'])
    new['tags'] = new['tags'].apply(lambda x: " ".join(x))
    cv = CountVectorizer(max_features=5000, stop_words='english')

    # vectorisation
    vector = cv.fit_transform(new['tags']).toarray()

    # cosine similarity
    similarity = cosine_similarity(vector)
    return new, similarity

