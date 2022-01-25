let side=document.querySelector("#Side");
let seatno=document.querySelector("#SeatNo");

function selectseat()
{
    if(side.value=="A")
    {
        seatno.innerHTML="";
        for(let i=1;i<=20;i++)
        {
            seatno.insertAdjacentHTML("beforeend","<option value="+i+">"+i+"</option>");
        }
    }
    else if(side.value=="B")
    {
        seatno.innerHTML="";
        for(let i=1;i<=10;i++)
        {
            seatno.insertAdjacentHTML("beforeend","<option value="+i+">"+i+"</option>");
        } 
    }
    else
    {
        seatno.innerHTML="";
        seatno.insertAdjacentHTML("beforeend","<option value='*'>*</option>");
    }
}
nepal=["Nepalgunj","Butwal","Dhangadi"]
india=["Maharashtra","Gujarat"]

let from=document.querySelector(".From");
let to=document.querySelector(".To");
function endingTo()
{
    let value=from.value;
    if(nepal.indexOf(value)>-1)
    {
        to.innerHTML="";
        for(let i=0;i<india.length;i++)
        {
            to.insertAdjacentHTML("beforeend",'<option name="'+india[i]+'" id="">'+india[i]+'</option>');
        }
    }
    else
    {
        to.innerHTML="";
        for(let i=0;i<nepal.length;i++)
        {
            to.insertAdjacentHTML("beforeend",'<option name="'+nepal[i]+'" id="">'+nepal[i]+'</option>');
        }
    }
}