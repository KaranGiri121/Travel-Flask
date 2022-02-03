const Lower=document.querySelector('.lower');
const Upper=document.querySelector(".upper");
const LSeats=document.querySelectorAll(".lower .berth .row .seat");
const USeats=document.querySelectorAll(".upper .berth .row .seat");
const count=document.querySelector(".count");
const total=document.querySelector('.total');

let price=2500;
//Reading Old Data
populateUI()

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
    localStorage.setItem('LSelected',JSON.stringify(LselectedIndex));
    localStorage.setItem('USelected',JSON.stringify(UselectedIndex));
    
    
    count.innerHTML=LselectedSeat.length+UselectedSeat.length;
    total.innerHTML=(LselectedSeat.length+UselectedSeat.length)*price;
    document.querySelector("button .total").innerHTML=(LselectedSeat.length+UselectedSeat.length)*price;
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
//Function For Reading Old Data
function populateUI()
{
    let x=JSON.parse(localStorage.getItem('LSelected'));
    for(let i=0;x!=null && i<x.length ;i++)
    {
        LSeats[x[i]].classList.toggle('selected');
    }
    let y=JSON.parse(localStorage.getItem("USelected"));
    for(let i=0;y!=null && i<y.length;i++)
    {
        USeats[y[i]].classList.toggle('selected');
    }
}

//Swtich Between Lower And Upper
let lowerButton=document.querySelector(".lower-button");
let upperButton=document.querySelector(".upper-button");
lowerButton.onclick=function()
{
    upperButton.disabled=!upperButton.disabled;
    lowerButton.disabled=!lowerButton.disabled;
    document.querySelector(".upper").style.display="none";
    document.querySelector('.lower').style.display="block";
}
upperButton.onclick=function()
{
    upperButton.disabled=!upperButton.disabled;
    lowerButton.disabled=!lowerButton.disabled;
    document.querySelector(".upper").style.display="block";
    document.querySelector('.lower').style.display="none";
}