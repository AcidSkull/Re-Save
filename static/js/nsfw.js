let nsfw = document.getElementsByClassName('nsfw');
let Titles = document.getElementsByClassName('title');

// Show a nsfw post image after click
for(let i = 0; i < nsfw.length; i++){
    nsfw[i].addEventListener('click', function() {
        this.classList.remove('nsfw');
    });
}


// Craeting array of two bools which determine whether show NSFW posts or SFW posts
let nsfw_buttons = document.getElementsByClassName('search_category');
let hide = [false, false]

for(let i = 0; i < 2; i++){
    nsfw_buttons[i].addEventListener('click', function(){
        hide[i] = !hide[i];
    });
}

// Creqating array with true for nsfw post and false for normal post
let nsfw_posts = [];
for(let i = 0; i < Titles.length; i++){
    if(Titles[i].textContent.includes('🔥 NSFW') == true)
        nsfw_posts[i] = true;
    else
        nsfw_posts[i] = false;
}