document.addEventListener("DOMContentLoaded", (e) => {
    console.log("Hello, world by app.js!");
});


const backLinks = document.querySelectorAll(".back-link");



backLinks.forEach((item) => {
    item.addEventListener("click", (e) => {
        e.preventDefault();
        console.log("back-link clicked");
        history.back();
    });
});