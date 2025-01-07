const axios = require('axios');
const path = require('path');
const moviesDataPath = path.join(__dirname, '../data/movies_cleaned.csv');

// Recommendations via the Flask API
exports.getRecommendations = async (req, res) => {
    const { movie_title } = req.body;

    try {
        const response = await axios.post('http://localhost:5001/recommend', { movie_title });
        res.status(200).json(response.data);
    } catch (error) {
        console.error("Error during API call:", error.message);
        res.status(500).json({ message: 'Error fetching recommendations' });
    }
};
