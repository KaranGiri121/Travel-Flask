const Lower=document.querySelector('.lower');
const Upper=document.querySelector(".upper");
const LSeats=document.querySelectorAll(".lower .berth .row .seat");
const USeats=document.querySelectorAll(".upper .berth .row .seat");
const count=document.querySelector(".count");
const total=document.querySelector('.total');

//Update Count And Total
function updateSelected()
{
    const LselectedSeat=document.querySelectorAll(".lower .berth .row .seat.selected");
    const UselectedSeat=document.querySelectorAll(".upper .berth .row .seat.selected");
    
    const LselectedIndex=[...LselectedSeat].map(function(seat){
        return [...LSeats].indexOf(seat);
    })
    const UselectedIndex=[...UselectedSeat].map(function(seat){
        return [...USeats].indexOf(seat);
    })

    document.pay.LSeat.value=JSON.stringify(LselectedIndex);
    document.pay.USeat.value=JSON.stringify(UselectedIndex);
    
    
    count.innerHTML=LselectedSeat.length+UselectedSeat.length;
    total.innerHTML=(LselectedSeat.length+UselectedSeat.length)*Price;
    document.querySelector("button .total").innerHTML=(LselectedSeat.length+UselectedSeat.length)*Price;
}

Lower.addEventListener("click",(e)=>{
    if(e.target.classList.contains('seat') && !e.target.classList.contains("booked"))
    {
        e.target.classList.toggle('selected');
    }
    updateSelected();
})
Upper.addEventListener("click",(e)=>{
    if(e.target.classList.contains('seat') && !e.target.classList.contains("booked"))
    {
        e.target.classList.toggle('selected');
    }
    updateSelected();
})

//Menu Toggle Button
let menu_button=document.querySelector('.menu');
let link=document.querySelector('.link')
menu_button.onclick = function(){
    menu_button.classList.toggle("active");
    link.classList.toggle('active');
}

//Swtich Between Lower And Upper
let lowerButton=document.querySelector(".lower-button");
let upperButton=document.querySelector(".upper-button");
lowerButton.onclick=function()
{
    upperButton.disabled=!upperButton.disabled;
    lowerButton.disabled=!lowerButton.disabled;
    document.querySelector(".upper").style.display="none";
    document.querySelector('.lower').style.display="flex";
}
upperButton.onclick=function()
{
    upperButton.disabled=!upperButton.disabled;
    lowerButton.disabled=!lowerButton.disabled;
    document.querySelector(".upper").style.display="flex";
    document.querySelector('.lower').style.display="none";
}
