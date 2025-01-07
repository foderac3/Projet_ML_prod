import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import mlflow
import mlflow.sklearn

# MLflow configuration for DagsHub
DAGSHUB_USERNAME = "foderac3"
DAGSHUB_TOKEN = "9d2d5d002b35632a47b9e353e2b33eb241370f9f"
REPO_NAME = "Projet_ML_prod"
TRACKING_URI = f"https://{DAGSHUB_USERNAME}:{DAGSHUB_TOKEN}@dagshub.com/{DAGSHUB_USERNAME}/{REPO_NAME}.mlflow"

mlflow.set_tracking_uri(TRACKING_URI)
mlflow.set_experiment("Movie_Recommendation_Experiment")


def train_model():
    movies_df = pd.read_csv("data/movies_cleaned.csv")

    # Encoding of 'genre' and 'director' columns
    column_transformer = ColumnTransformer(
        transformers=[
            ('genre', OneHotEncoder(), ['genre']),
            ('director', OneHotEncoder(), ['director'])
        ]
    )

    # Model training and similarity matrix calculation
    with mlflow.start_run():
        print("Entraînement du modèle...")
        features_matrix = column_transformer.fit_transform(movies_df[['genre', 'director']])
        similarity_matrix = cosine_similarity(features_matrix)

        # Parameter and metrics log
        mlflow.log_param("columns_encoded", ['genre', 'director'])
        mlflow.log_metric("matrix_shape", features_matrix.shape[0])

        # Saving the model locally
        joblib.dump(column_transformer, "model_encoder.pkl")
        np.save("similarity_matrix.npy", similarity_matrix)

        # Log artifacts in DagsHub
        mlflow.log_artifact("model_encoder.pkl")
        mlflow.log_artifact("similarity_matrix.npy")

        # Saving the model in MLflow
        mlflow.sklearn.log_model(column_transformer, "encoder_model")

        print("Modèle entraîné et sauvegardé sur DagsHub.")


if __name__ == "__main__":
    train_model()
