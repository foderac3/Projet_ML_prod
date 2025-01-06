from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn

app = Flask(__name__)
CORS(app)

# Charger les données du CSV
movies_df = pd.read_csv("data/movies_cleaned.csv")

# Configuration MLflow pour DagsHub (identifiants fournis)
mlflow.set_tracking_uri("https://foderac3:9d2d5d002b35632a47b9e353e2b33eb241370f9f@dagshub.com/foderac3/Projet_ML_prod.mlflow")

# Utilisation du run ID connu pour charger le modèle
run_id = "13e263c276fa4a94b18a1c072725be16"
logged_model_uri = f"runs:/{run_id}/encoder_model"

try:
    print(f"Loading model from run: {run_id}")
    column_transformer = mlflow.sklearn.load_model(logged_model_uri)
except Exception as e:
    raise Exception(f"Erreur lors du chargement du modèle MLflow : {e}")

# Charger la matrice de similarité
similarity_matrix = np.load("similarity_matrix.npy")

# Fonction de recommandation basée sur la similarité cosinus
def get_recommendations(movie_title, top_n=5):
    try:
        idx = movies_df[movies_df['name'] == movie_title].index[0]
        sim_scores = list(enumerate(similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        top_indices = [i[0] for i in sim_scores[1:top_n+1]]
        return movies_df['name'].iloc[top_indices].tolist()
    except IndexError:
        return ["Film non trouvé"]

# Route API pour obtenir des recommandations
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_title = data.get('movie_title')

    if not movie_title:
        return jsonify({'error': 'Le titre du film est requis'}), 400

    recommendations = get_recommendations(movie_title)
    return jsonify({'recommendations': recommendations})

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(port=5001)
