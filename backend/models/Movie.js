const mongoose = require('mongoose');

const MovieSchema = new mongoose.Schema({
    name: String,
    genre: String,
    director: String,
    budget: Number,
    gross: Number,
    released: Date
});

module.exports = mongoose.model('Movie', MovieSchema);
