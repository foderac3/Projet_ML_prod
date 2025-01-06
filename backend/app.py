from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)  # Active CORS pour éviter les problèmes de politique de sécurité

# Charger les données et le modèle
movies_df = pd.read_csv("data/movies_cleaned.csv")
similarity_matrix = np.load("similarity_matrix.npy")
column_transformer = joblib.load("model_encoder.pkl")

# Fonction de recommandation
def get_recommendations(movie_title, top_n=5):
    try:
        idx = movies_df[movies_df['name'] == movie_title].index[0]
        sim_scores = list(enumerate(similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        top_indices = [i[0] for i in sim_scores[1:top_n+1]]
        return movies_df['name'].iloc[top_indices].tolist()
    except IndexError:
        return ["Film non trouvé"]

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.json.get('movie_title')
    recommendations = get_recommendations(movie_title)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(port=5001)
