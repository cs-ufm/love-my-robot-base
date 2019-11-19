const express = require('express');
const redis = require('redis');
const publisher = redis.createClient();
const app = express();
const port = 8080;

app.get('/', (req, res) => res.send('Hello From Express'));

app.listen(port, () => console.log(`Example app listening on port ${port}!`));

var j={
    "name":"Andrea"
};

function JSONpub(json) {
    console.log("Sending JSON")
    json_string = JSON.stringify(json)
    publisher.publish("test",json_string);
}

JSONpub(j)