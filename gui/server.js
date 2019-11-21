const express = require('express')
const app = express()
//var path = require('path')
const Mustache = require('mustache')
const fs = require('fs')
const port = 8080

app.use(express.static('public'))

app.get('/', function(req, res){
    const template = fs.readFileSync('views/index.html', 'utf8');

    // get keys for todo
    const keys_string = fs.readFileSync('./keys.json', 'utf8');
    const keys = JSON.parse(keys_string);

    for (let key in keys) {
        keys[key].gap = ((parseInt(key) + 1) * 140) - 20
    }

    //include menu.html
    const menu = fs.readFileSync('views/menu.html', 'utf8');

    //include navbar.html
    const nav = fs.readFileSync('views/navbar.html', 'utf8');

    //include container.html
    const con = fs.readFileSync('views/container.html', 'utf8');

    //include jumbotron.html
    const jumbo = fs.readFileSync('views/jumbotron.html', 'utf8');

    //include modal.html
    const modal = fs.readFileSync('views/modal.html', 'utf8');

    const renderIndex = Mustache.render(template, {menuOptions: keys}, {menu, nav, jumbo, con, modal});

    res.status(200).send(renderIndex)
})


//app.get('/', (req, res) => res.send('Hello From Express'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))