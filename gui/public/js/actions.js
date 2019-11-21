let actions = ["move", "sounds", "cozmo-lights", "animations"]
$( document ).ready(function() {
    for (let i = 0; i < actions.length; i++) {
        $(`.${actions[i]}`).click(function(){
            console.log("clicked")
            document.getElementsByClassName(actions[i])[1].classList.remove('hide')

            for (let j = 0; j < actions.length; j++){
                if(j != i){
                    document.getElementsByClassName(actions[j])[1].classList.add('hide')
                }
            }
        });
    }
});