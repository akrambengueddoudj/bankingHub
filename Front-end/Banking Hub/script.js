// ========================== jquery for navbar background ================ 
$(function(){
    $(document).scroll(function(){
        var $nav = $('.nav');
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

// ============================== toggler menu ======================= 
var menu = document.getElementById('bar');
var items = document.getElementById('navbar');
items.style.left= "-360px";

menu.onclick = function(){
    if (items.style.left== "-360px"){
        items.style.left= "0";
    }
    else{
        items.style.left= "-360px";
    }

}

