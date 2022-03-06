Posts = document.getElementsByClassName('post')
Titles = document.getElementsByClassName('title');
Searchbox = document.getElementById('searchbox');

let search = function (){
    // Seting regular expression equal to text in search bar
    let pattern = document.getElementById('searchbox').value;
    let regex = new RegExp(pattern, "ig")

    // Looping through all posts and checking if title is equal to regex pattern or if searchbox is empty, then if true make post visible
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