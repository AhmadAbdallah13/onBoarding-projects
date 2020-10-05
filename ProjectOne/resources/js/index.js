
function onSubmit() {
    txt = document.getElementById("txt").value;
    colo = document.getElementById("colo").value;
    num = document.getElementById("num").value;
    rep = document.getElementById("rep").value;

    var ogP = document.getElementById('addOnMe')
    if (ogP.innerHTML == 'Empty as a broken water jar') ogP.innerHTML = ''
    ogP.style.fontSize = parseInt(num) + 'px';
    ogP.style.color = colo;
    for(var i = 1; i <= rep; i++)
    {
        ogP.innerHTML += txt + "<br>"
    }
   
}
