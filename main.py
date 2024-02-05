from MoviRecommender import generate_similarity
from MainApp import web
import pickle
import os

def pickle1(new,similarity):
    pickle.dump(new, open('movie_list.pkl', 'wb'))
    pickle.dump(similarity, open('similarity.pkl', 'wb'))
    print("done")

if __name__ == '__main__':
    files_to_check = ['movie_list.pkl', 'similarity.pkl']
    if os.path.exists(files_to_check[0]) and os.path.exists(files_to_check[1]):
        web(files_to_check[0],files_to_check[1])
        os.system("streamlit run C:\\Users\\Adity\\PycharmProjects\\RecommenderSystem\\main.py --server.port 8502")
    else:
        new,similarity = generate_similarity()
        pickle1(new, similarity)
        web(files_to_check[0],files_to_check[1])
        os.system("streamlit run C:\\Users\\Adity\\PycharmProjects\\RecommenderSystem\\main.py --server.port 8502")





