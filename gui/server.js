const express = require('express')
const app = express()
//var path = require('path')
const Mustache = require('mustache')
const fs = require('fs')
const port = 8080

app.use(express.static('public'))

app.get('/', function(req, res){
    const template = fs.readFileSync('views/index.html', 'utf8');

    // get info fron todo.json
    const todo_string = fs.readFileSync('./todo.json', 'utf8');
    const actions = JSON.parse(todo_string);

    // get keys for todo
    const keys_string = fs.readFileSync('./keys.json', 'utf8');
    const keys = JSON.parse(keys_string);

    //include menu.html
    const menu = fs.readFileSync('views/menu.html', 'utf8');

    const renderIndex = Mustache.render(template, {menuOptions: keys}, {menu});

    res.status(200).send(renderIndex)
})


//app.get('/', (req, res) => res.send('Hello From Express'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))