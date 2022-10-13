const express = require("express");
var path = require('path');
const app = express();
const PORT = 8080;


app.use(express.urlencoded({extended: true}));

app.listen(PORT, () => {
 console.log('Server is running on port: ' + PORT);
});

app.get('/', function (req, res) {

    var indexFile = path.join(__dirname, '/', 'index.html');
    res.sendFile(indexFile)
});
