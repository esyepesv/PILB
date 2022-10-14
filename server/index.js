const express = require("express");
var path = require('path');
const http = require("http");
const app = express();
const PORT = 8080;

const host = 'localhost';


app.use(express.urlencoded({extended: true}));

app.listen(PORT, host, () => {
 console.log('Server is running on port: ' + PORT);
});

app.get('/', function (req, res) {

    var indexFile = path.join(__dirname, '/', 'index.html');
    res.sendFile(indexFile)
});
