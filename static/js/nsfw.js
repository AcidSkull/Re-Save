let nsfw = document.getElementsByClassName('nsfw');
let Titles = document.getElementsByClassName('title');

// Show a nsfw post image after click
for(let i = 0; i < nsfw.length; i++){
    nsfw[i].addEventListener('click', function() {
        this.classList.remove('nsfw');
    });
}