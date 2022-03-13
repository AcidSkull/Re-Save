let button = document.getElementsByClassName('settings');
let menu = document.getElementById('hidden_menu');

// Opening/closing accordion menu
button[0].addEventListener('click', function(){
    if(menu.style.maxHeight == menu.scrollHeight + 'px')
        menu.style.maxHeight = 0; 
    else 
        menu.style.maxHeight = menu.scrollHeight + 'px';
});

// Function to filter unique values from array
const Unique = (value, index, self) => {
    return self.indexOf(value) === index;
}

// Creating array with names of subreddits
let subreddit = document.getElementsByClassName('subreddit');
let subreddits = new Array;
for(let i = 0; i < subreddit.length; i++){
    subreddits[i] = subreddit[i].innerHTML;
}

// Creating array with unique subreddits names
let subreddits_unique = subreddits.filter(Unique);

// Creating buttons in hidden menu
for(let i = 0; i < subreddits_unique.length; i++){
    menu.innerHTML += `<div class="category">${subreddits_unique[i]}</div>`;
}

// Hide unwanted posts
let flags = [];
function hide(){
    let posts = document.getElementsByClassName('post');
    let sub = document.getElementsByClassName('subreddit');

    for(let i = 0; i < posts.length; i++){
        if(flags.length == 0) {
            posts[i].style.display = '';
            continue;
        }

        for(let j = 0; j < flags.length; j++){
            if(sub[i].textContent == flags[j]){
               posts[i].style.display = ''; 
               break;
            } else {
                posts[i].style.display = 'none'; 
            }
        }
    }
}

// Adding click event to all subreddits buttons
let category = document.getElementsByClassName('category');
for(let i = 0; i < category.length; i++){
    category[i].addEventListener('click', function(){
        this.classList.toggle('chosen');
        
        if(this.classList.contains('chosen') == true){
            flags.push(this.textContent);
        } else {
            let to_delete = flags.indexOf(this.textContent);
            flags.splice(to_delete, 1);
        }
        hide();
    });
}