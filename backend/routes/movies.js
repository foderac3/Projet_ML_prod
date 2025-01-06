const express = require('express');
const router = express.Router();
const movieController = require('../controllers/movieController');

router.post('/recommend', movieController.getRecommendations);

module.exports = router;
