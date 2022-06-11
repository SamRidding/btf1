const burgerMenu = document.getElementById('burger');
const navLinks = document.getElementsByClassName('navbar-links')[0];

burgerMenu.addEventListener('click', e => {
    navLinks.classList.toggle('active')
});


const searchBtn = document.getElementById('search-btn');
const searchBar = document.getElementById('search');

searchBtn.addEventListener('click', e => {
    if (searchBar.style.display === 'none') {
        searchBar.style.display = 'flex';
    } else {
        searchBar.style.display = 'none';
    }
});

