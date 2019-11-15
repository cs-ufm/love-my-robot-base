const express = require('express')
const app = express()
//var path = require('path')
const Mustache = require('mustache')
const fs = require('fs')
const port = 8080

let actions = ['Fernando Gonzalez']

app.use(express.static('public'))

app.get('/', function(req,res){
    const template = fs.readFileSync('templates/index.html', 'utf8');

    const renderIndex = Mustache.render(template, {actions});

    res.status(200).send(renderIndex)
})


//app.get('/', (req, res) => res.send('Hello From Express'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))