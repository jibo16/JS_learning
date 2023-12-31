function getRandom(){
    var letters = "0123456789ABCDEF";
    var color ='#';
    var x = 0;
    
    while (x < 6){
      color += letters[Math.floor(Math.random()*16)];
      x++;
    }
    return color
  }
  

function randomizer(){


var head = document.querySelector("h1")
head.style.color = String(getRandom());

}

setInterval("randomizer()",800)