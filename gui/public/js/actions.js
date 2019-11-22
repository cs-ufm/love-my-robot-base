let actions = ["move", "sounds", "cozmo-lights", "animations"]
$( document ).ready(function() {

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

    // update code from modal
    //$(".subli").click(function(){
    //        let putInStack = document.getElementsByClassName(actions[i])[1].classList.remove('hide') }
    //    });
});