const toggleButton = document.getElementsByClassName("toggle-button")[0];
const navbarLinks = document.getElementsByClassName("navbar-links")[0];
toggleButton.addEventListener("click", () => {
    navbarLinks.classList.toggle("active");
});


$(document).ready(function() {
    $(".close").click(function() {
        $(this).parent().hide();
    });
});