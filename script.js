var express = require('express');
var mysql = require('mysql');
//Initialize Express
var app = express();


var bodyParser = require('body-parser')
var session = require('express-session')
var ejs = require('ejs')
var morgan = require('morgan')
var config = require('./script')



app.use(express.static('public'))
app.set('view engine','ejs')
app.use(morgan('tiny'))
app.use(bodyParser.urlencoded({ extended: false }))


// Intialize Session
app.use(session({
  secret: 'keyboard cat',
  resave: true,
  saveUninitialized: true,
  cookie: { secure: false }
}))

// Initialize express-flash
app.use(require('express-flash')());

// Routing
app.use('/',require('./routes/app')())





// sets port 8080 to default or unless otherwise specified in the environment
app.set('port', process.env.PORT || 8080);

app.listen(app.get('port'));
