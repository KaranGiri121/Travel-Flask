let menu_button=document.querySelector('.menu');
let link=document.querySelector('.link')
menu_button.onclick = function(){
    menu_button.classList.toggle("active");
    link.classList.toggle('active');
}

let ind=document.querySelector(".indiabutton");
let nep=document.querySelector(".nepalbutton");


function toggleblock()
{
    ind.disabled=!ind.disabled;
    nep.disabled=!nep.disabled;
}

ind.onclick=function(){
    toggleblock();
    document.querySelector("#NepalTour").style.display="none";
    document.querySelector("#IndiaTour").style.display="block"; 
}
nep.onclick=function(){
    toggleblock();
    document.querySelector("#NepalTour").style.display="block";
    document.querySelector("#IndiaTour").style.display="none"; 
}
