let menu_button=document.querySelector('.menu');
let link=document.querySelector('.link')
menu_button.onclick = function(){
    menu_button.classList.toggle("active");
    link.classList.toggle('active');
}