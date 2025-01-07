import React, { useState } from 'react';
import axios from 'axios';
import styles from '../../styles/Home.module.css';

const Home = () => {
    const [movieTitle, setMovieTitle] = useState('');
    const [recommendations, setRecommendations] = useState([]);

    const handleRecommend = async () => {
        if (!movieTitle) {
            alert("Please enter a movie title : ");
            return;
        }

        try {
            const response = await axios.post('http://localhost:5001/recommend', {
                movie_title: movieTitle
            });

            setRecommendations(response.data.recommendations);
        } catch (error) {
            console.error("Query error :", error);
            alert("Unable to retrieve recommendations.");
        }
    };

    return (
        <div className={styles.container}>
            <h1 className={styles.title}>Recommander un Film</h1>
            <input
                type="text"
                className={styles.input}
                value={movieTitle}
                onChange={(e) => setMovieTitle(e.target.value)}
                placeholder="Name of film"
            />
            <button onClick={handleRecommend} className={styles.button}>
                Recommander
            </button>

            <div className={styles.result}>
                <h2>Résultats :</h2>
                <ul>
                    {recommendations.map((rec, index) => (
                        <li key={index} className={styles.listItem}>{rec}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Home;
