var table = document.getElementById("table");
var tbody = document.getElementById("tbody");
var highestTrId = 0;

function addWord() {
    var newRow = document.createElement("tr");

    var cell1 = document.createElement("td");
    var cell2 = document.createElement("td");
    var cell3 = document.createElement("td");
    var cell4 = document.createElement("td");

    var input1 = document.createElement("input");
    input1.type = "text";
    input1.name = "polish[]";
    cell1.appendChild(input1);

    var dashElement = document.createElement("b");
    dashElement.innerHTML = "-";
    cell2.appendChild(dashElement);

    var input2 = document.createElement("input");
    input2.type = "text";
    input2.name = 'english[]';
    cell3.appendChild(input2);

    var trashIcon = document.createElement("i");
    trashIcon.className = "bi bi-trash";
    trashIcon.onclick = function(){
        deleteWord(this);
    };
    cell4.appendChild(trashIcon);

    newRow.id = highestTrId;
    newRow.appendChild(cell1);
    newRow.appendChild(cell2);
    newRow.appendChild(cell3);
    newRow.appendChild(cell4);

    tbody.appendChild(newRow);

    setRowsId();
}

function deleteWord(iElement){
    if(document.querySelectorAll('tr').length > 3){
        var parentTd = iElement.parentNode;
        var parentTr = parentTd.parentNode;
        parentTr.remove();
        setRowsId();
    }
}

function setRowsId(){
    var elements = document.querySelectorAll('tr');

    for (var element of elements){
        element.id = highestTrId;
        highestTrId++;
    }

    highestTrId = 0;
}

setRowsId();