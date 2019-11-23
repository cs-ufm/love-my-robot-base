let actions = ["move", "sounds", "cozmo-lights", "animations"]
$( document ).ready(function() {
    console.log("document on")
    // display and hide options from menu
    for (let i = 0; i < actions.length; i++) {
        $(`.${actions[i]}`).click(function(){
            document.getElementsByClassName(actions[i])[1].classList.remove('hide')

            for (let j = 0; j < actions.length; j++){
                if(j != i){
                    document.getElementsByClassName(actions[j])[1].classList.add('hide')
                }
            }
        });
    }    
});
$( window ).on( "load", function() {
    console.log( "window loaded" );

    // put li instack with its attributes
    $(".push-to-stack").click(function(event){
        $("#cozmo-stack").append('<li class="list-group-item" code='+event.target.getAttribute("code")+'>'+event.target.name+'</li>');
        let newItem = event.target.getAttribute("code")
        //console.log(newItem)
        //let test = {name : "test"}
        //console.log("antes de entrar");
        $.post('/task-added', {name:newItem}, function(data,status){
            alert("Data: " + data + "\nStatus: " + status);
        }); 
        
        
        /*data = {"name":"victor"};
        var posting = $.post( "/task-added", data );
        console.log(posting);
        */
        console.log(newItem)
    });
});