function add(){
    var value1 = document.getElementById('value1').value;
    var value2 = document.getElementById('value2').value;

    var result = parseFloat(value1) + parseFloat(value2)
    document.getElementById('result').value = result
}
function subtract(){
    var value1 = document.getElementById('value1').value;
    var value2 = document.getElementById('value2').value;

    var result = parseFloat(value1) - parseFloat(value2)
    document.getElementById('result').value = result
}
function multiply(){
    var value1 = document.getElementById('value1').value;
    var value2 = document.getElementById('value2').value;

    var result = parseFloat(value1) * parseFloat(value2)
    document.getElementById('result').value = result
}
function divide(){
    var value1 = document.getElementById('value1').value;
    var value2 = document.getElementById('value2').value;

    var result = parseFloat(value1) / parseFloat(value2)
    document.getElementById('result').value = result
}