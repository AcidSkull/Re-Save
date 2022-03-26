let button = document.getElementsByClassName('settings');
let menu = document.getElementById('hidden_menu');

// Opening/closing accordion menu
button[0].addEventListener('click', function(){
    if(menu.style.maxHeight == menu.scrollHeight + 'px'){
        menu.style.maxHeight = 0;
        menu.style.paddingBottom = 0;
    } else {
        menu.style.maxHeight = menu.scrollHeight + 20 + 'px';
        menu.style.paddingBottom = "20px";
    }
});

// Setting hidden menu below navbar
let navbar = document.getElementById('navbar');
menu.style.top = navbar.scrollHeight - 10 + "px";

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
    menu.innerHTML += `<div class="search_category category">${subreddits_unique[i]}</div>`;
}