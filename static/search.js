Posts = document.getElementsByClassName('post')
Titles = document.getElementsByClassName('title');
Searchbox = document.getElementById('searchbox');

let search = function (){
    let pattern = document.getElementById('searchbox').value;
    let regex = new RegExp(pattern, "ig")

    for(let i = 0; i < Titles.length; ++i){
        if(regex.test(Titles[i].textContent) || pattern == ''){
            Posts[i].style.display = '';
        } else {
            Posts[i].style.display = 'none';
        }
    }
}

Searchbox.addEventListener('input', search);
Searchbox.addEventListener('keydown', search);