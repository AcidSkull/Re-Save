Posts = document.getElementsByClassName('posts')
Titles = document.getElementsByClassName('title');

function Search_Site(){
    let pattern = document.getElementById('searchbox');

    for(let i = 0; i < Titles.length; ++i){
        if(Titles.textContent == pattern || pattern == ""){
            Posts[i].style.display = 'none';
        } else {
            Posts[i].style.display = '';
        }
    }
}