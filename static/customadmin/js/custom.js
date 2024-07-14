let states = []
let inputStates = []
function stateHolder(stateid,statename){
    if (states.includes(stateid)){
        states.pop(states.indexOf(stateid))
        inputStates.pop(states.indexOf(statename))
        document.getElementById(stateid).classList.remove('selecected')
    }else{
            states.push(stateid)
            inputStates.push(statename)
            document.getElementById(stateid).classList.add('selecected')
    }
    document.getElementById("selectedStates").value = inputStates
    document.getElementById("stateSelectedId").value = states
}

function showHideMenue(){
    document.getElementById('Statemenue').classList.toggle('hide')
}