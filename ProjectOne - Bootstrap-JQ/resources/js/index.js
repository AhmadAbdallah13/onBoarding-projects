$( "#btn" ).click(function() {
    txt = $( "#txt" ).val()
    colo = $( "#colo" ).val()
    num = $( "#num" ).val()
    rep = $( "#rep" ).val()
    paraElement = $( "#addOnMe" )
    
    if (paraElement.html() == 'Empty as a broken water jar') paraElement.text('')

    paraElement.css( "color", colo );
    paraElement.css( "font-size", parseInt(num) );

    for(var i = 1; i <= rep; i++)
    {
        paraElement.html( paraElement.html() + txt + "<br>")
    }
  })

  $( "#clickMe" ).click(function() {
    alert('ta da')
  })