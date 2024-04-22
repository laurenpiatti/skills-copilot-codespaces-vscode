// Create web server

// Import the express module
var express = require('express');
// Create an express application
var app = express();
// Import the body-parser module
var bodyParser = require('body-parser');
// Import the mongoose module
var mongoose = require('mongoose');

// Connect to the MongoDB database
mongoose.connect('mongodb://localhost/comments');

// Create a new schema
var commentSchema = new mongoose.Schema({
    name: String,
    comment: String,
    date: Date
});

// Create a new model
var Comment = mongoose.model('Comment', commentSchema);

// Set the view engine to ejs
app.set('view engine', 'ejs');

// Use the body-parser middleware
app.use(bodyParser.urlencoded({extended: true}));

// Use the express.static middleware
app.use(express.static('public'));