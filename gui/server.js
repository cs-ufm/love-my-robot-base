const express = require('express')
const app = express()
//var path = require('path')
var bodyParser = require('body-parser');
const Mustache = require('mustache')
const fs = require('fs')
const port = 8080

app.use(express.static('public'))

let act = ['Jose', 'Luis']  

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

    //include stack.html
    const stack = fs.readFileSync('views/stack.html', 'utf8');

    //include jumbotron.html
    const jumbo = fs.readFileSync('views/jumbotron.html', 'utf8');

    //include modal.html
    const modal = fs.readFileSync('views/modal.html', 'utf8');

    const renderIndex = Mustache.render(template, {menuOptions: keys}, {menu, nav, jumbo, stack, modal});

    res.status(200).send(renderIndex)
})

app.get('/home', function (req, res) {

    // include home.html
    const template = fs.readFileSync('views/home.html', 'utf8');

    // get keys for todo
    const keys_string = fs.readFileSync('./keys.json', 'utf8');
    const keys = JSON.parse(keys_string);

   
    //include navbar.html
    const nav = fs.readFileSync('views/navbar.html', 'utf8');

    //include jumbotron.html
    const jumbo = fs.readFileSync('views/jumbotron.html', 'utf8');

    const renderIndex = Mustache.render(template, {
        menuOptions: keys
    }, {
        nav,
        jumbo
    });

    res.status(200).send(renderIndex)
})


app.get('/actions', function (req, res) {

    const template = fs.readFileSync('views/index.html', 'utf8');

    // get keys for todo
    const keys_string = fs.readFileSync('./keys.json', 'utf8');
    const keys = JSON.parse(keys_string);

    const action_string = fs.readFileSync('./actions.json', 'utf8');
    const actions = JSON.parse(action_string);

    //To add a value to our json
    //actions['actions'].push("Jump")

    for (let key in keys) {
        keys[key].gap = ((parseInt(key) + 1) * 140) - 20
    }

    //include menu.html
    const menu = fs.readFileSync('views/menu.html', 'utf8');

    //include navbar.html
    const nav = fs.readFileSync('views/navbar.html', 'utf8');

    //include stack.html
    const stack = fs.readFileSync('views/stack.html', 'utf8');

    //include jumbotron.html
    const jumbo = fs.readFileSync('views/jumbotron.html', 'utf8');

    //include modal.html
    const modal = fs.readFileSync('views/modal.html', 'utf8');

    const renderIndex = Mustache.render(template, {
        menuOptions: keys, actions_test: actions
    }, {
        menu,
        nav,
        jumbo,
        stack,
        modal
    });

    res.status(200).send(renderIndex)
})

app.post('/task-added', function(req, res){
    console.log(req.body);
    act.push(req.body.name);

})


//app.get('/', (req, res) => res.send('Hello From Express'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))