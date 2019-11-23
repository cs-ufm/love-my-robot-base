function lex() {

    let name = {
        "actions": "hello"
    }

    $.post('/Lex', name, function () {

        if (!alert('Posting....\n')) { //Reload page automatic
            window.location.reload();
        }


    });
}