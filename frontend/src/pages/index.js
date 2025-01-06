import React, { useState } from 'react';
import axios from 'axios';

const Home = () => {
    const [movieTitle, setMovieTitle] = useState('');
    const [recommendations, setRecommendations] = useState([]);

    const handleRecommend = async () => {
        if (!movieTitle) {
            alert("Veuillez entrer un titre de film : ");
            return;
        }

        try {
            const response = await axios.post('http://localhost:5001/recommend', {
                movie_title: movieTitle
            });

            setRecommendations(response.data.recommendations);
        } catch (error) {
            console.error("Erreur lors de la requête :", error);
            alert("Impossible de récupérer les recommandations.");
        }
    };

    return (
        <div>
            <h1>Recommander un Film</h1>
            <input
                type="text"
                value={movieTitle}
                onChange={(e) => setMovieTitle(e.target.value)}
                placeholder="Nom du film"
            />
            <button onClick={handleRecommend}>Recommander</button>

            <h2>Résultats :</h2>
            <ul>
                {recommendations.map((rec, index) => (
                    <li key={index}>{rec}</li>
                ))}
            </ul>
        </div>
    );
};

export default Home;
