let Posts = document.getElementsByClassName('post')
let Titles = document.getElementsByClassName('title');
let Searchbox = document.getElementById('searchbox');
let sub = document.getElementsByClassName('subreddit');

// Array with subreddits names to show
let categories_to_show = [];

function hide_it(){
    // Seting regular expression equal to text in search bar
    let pattern = document.getElementById('searchbox').value;
    let regex = new RegExp(pattern, "ig")
    
    for(let i = 0; i < Posts.length; ++i){
        if((regex.test(Titles[i].textContent) || pattern == '') && 
        (categories_to_show.length == 0 || categories_to_show.find(e => e == sub[i].textContent))){
            Posts[i].style.display = '';
        } else {
            Posts[i].style.display = 'none';
        }
    }
}

// Event listeners for searchbox
Searchbox.addEventListener('input', hide_it);
Searchbox.addEventListener('keydown', hide_it); 

// Showing post only from certain subreddit
let category = document.getElementsByClassName('category');
for(let i = 0; i < category.length; i++){
    category[i].addEventListener('click', function(){
        this.classList.toggle('chosen');
        
        if(this.classList.contains('chosen') == true){
            categories_to_show.push(this.textContent);
        } else {
            let to_delete = categories_to_show.indexOf(this.textContent);
            categories_to_show.splice(to_delete, 1);
        }
        hide_it();
    });
}