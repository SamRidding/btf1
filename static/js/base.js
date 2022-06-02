const burgerMenu = document.getElementById('burger');
const navLinks = document.getElementsByClassName('navbar-links')[0];

burgerMenu.addEventListener('click', e => {
    navLinks.classList.toggle('active')
});