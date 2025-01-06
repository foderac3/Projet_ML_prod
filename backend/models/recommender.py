import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib

def train_model():
    # Charger les données
    movies_df = pd.read_csv("data/movies_cleaned.csv")
    
    # Encodage des colonnes 'genre' et 'director'
    column_transformer = ColumnTransformer(
        transformers=[
            ('genre', OneHotEncoder(), ['genre']),
            ('director', OneHotEncoder(), ['director'])
        ]
    )

    # Matrice de caractéristiques
    features_matrix = column_transformer.fit_transform(movies_df[['genre', 'director']])
    
    # Calcul de la similarité cosinus
    similarity_matrix = cosine_similarity(features_matrix)

    # Sauvegarde du modèle et de la matrice
    joblib.dump(column_transformer, "model_encoder.pkl")
    np.save("similarity_matrix.npy", similarity_matrix)

    print("Modèle entraîné et fichiers sauvegardés.")

if __name__ == "__main__":
    train_model()
