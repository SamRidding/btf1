const burgerMenu = document.getElementById('burger');
const navLinks = document.getElementsByClassName('navbar-links')[0];

burgerMenu.addEventListener('click', e => {
    navLinks.classList.toggle('active')
});


const searchBtn = document.getElementById('search-btn');
const searchBar = document.getElementsByClassName('search')[0];

searchBtn.addEventListener('click', e => {
    searchBar.classList.toggle('active')
});

