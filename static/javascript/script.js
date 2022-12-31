let firstState = document.getElementById('first');
let finalState = document.getElementById('final');
let submit = document.getElementById('sub');
let userFirstState;
let userFinalState;
let firstStateArr = [[], [], []];
let finalStateArr = [[], [], []];

submit.addEventListener('click', function() {
    let counter = 0;

    len1 = firstState.value.length;
    len2 = finalState.value.length;

    if(len1 == 17 && len2 == 17){
        userFirstState = firstState.value.split(' ');
        userFinalState = finalState.value.split(' ');
        firstState.value = '';
        finalState.value = '';

        for(let i = 0; i < 3; i++){
            for(let j = 0; j < 3; j++){
                firstStateArr[i][j] = userFirstState[counter];
                finalStateArr[i][j] = userFinalState[counter++];
            }
        }
    }
    else {
        window.alert("ERROR");
    }
})