document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a[href*='skill-list']").forEach(link => {
        link.addEventListener("click", function (e) {
            localStorage.setItem("scrollPosition", window.scrollY);
        });
    });

    let scrollPosition = localStorage.getItem("scrollPosition");
    if (scrollPosition) {
        window.scrollTo(0, scrollPosition);
        localStorage.removeItem("scrollPosition");
    }
});
