
let leftlowerseats=document.querySelectorAll(".lowerberth .berthcontainer .left");
let leftupperseats=document.querySelectorAll(".upperberth .berthcontainer .left");

var count=1;
for(let i=0;i<leftlowerseats.length;i++)
{
    for(let x=0;x<2;x++)
    {
        leftlowerseats[i].insertAdjacentHTML("beforeend",'<div class="seat" id="B'+count+'">'+count+'</div>');
        leftupperseats[i].insertAdjacentHTML("beforeend",'<div class="seat" id="B_'+count+'">'+count+'</div>');
        count+=1;
    }

}
let rightseats=document.querySelectorAll(".lowerberth .berthcontainer .right");
let rightupperseats=document.querySelectorAll(".upperberth .berthcontainer .right");
count=1;
for(let i=0;i<rightseats.length;i++)
{
    for(let x=0;x<4;x++)
    {
        rightseats[i].insertAdjacentHTML("beforeend",'<div class="seat" id="A'+count+'">'+count+'</div>');
        rightupperseats[i].insertAdjacentHTML("beforeend",'<div class="seat" id="A_'+count+'">'+count+'</div>');
        count+=1;
    }
}


let lowerdisplay=document.querySelector(".lower");
let upperdisplay=document.querySelector(".upper");
let lowercontainer=document.querySelector(".lowerberth");
let uppercontainer=document.querySelector(".upperberth");

lowerdisplay.onclick=function()
{
    lowerdisplay.disabled=true;
    upperdisplay.disabled=false;
    lowercontainer.style.display="grid";
    uppercontainer.style.display="none";
    
}
upperdisplay.onclick=function()
{
    upperdisplay.disabled=true;
    lowerdisplay.disabled=false;
    lowercontainer.style.display="none";
    uppercontainer.style.display="grid";
}
