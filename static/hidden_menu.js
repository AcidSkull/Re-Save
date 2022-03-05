button = document.getElementsByClassName('settings')
menu = document.getElementById('hidden_menu');

button[0].addEventListener('click', function(){
    if(menu.style.maxHeight == menu.scrollHeight + 'px')
        menu.style.maxHeight = 0; 
    else 
        menu.style.maxHeight = menu.scrollHeight+'px';
});