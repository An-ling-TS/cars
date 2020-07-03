


var doms=$("[class=headline]")
//alert(doms[0].innerHTML)
var shines=[]
window.onload=function(){
    /**/
    for(var i=0;i<doms.length;i++){
        var shine = new Shine(doms[i]);
        alert(doms[i].innerHTML)
        shines.push(shine)
    }
    /**/
}
function handleMouseMove(event) {
    
    for(var i=0;i<shines.length;i++){
        shines[i].light.position.x = event.clientX;
        shines[i].light.position.y = event.clientY;
        shines[i].draw();
    }
}

window.addEventListener('mousemove', handleMouseMove, false);
