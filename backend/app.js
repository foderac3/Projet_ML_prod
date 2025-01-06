const express = require('express');
const app = express();
const moviesRoutes = require('./routes/movies');

// Middleware
app.use(express.json());

// Routes
app.use('/api/movies', moviesRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
