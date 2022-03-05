Posts = document.getElementsByClassName('post')
Titles = document.getElementsByClassName('title');
Searchbox = document.getElementById('searchbox');


Searchbox.addEventListener('input', () => {
    let pattern = document.getElementById('searchbox').value;

    for(let i = 0; i < Titles.length; ++i){
        if(Titles.textContent == pattern || pattern == ""){
            Posts[i].style.display = 'none';
        } else {
            Posts[i].style.display = '';
        }
    }
});