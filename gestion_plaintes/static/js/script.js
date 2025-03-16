document.addEventListener("DOMContentLoaded", function () {
    let slideIndex = 0;
    const slides = document.querySelectorAll(".slide");

    function showSlides() {
        slides.forEach(slide => slide.style.display = "none");
        slideIndex++;
        if (slideIndex > slides.length) { slideIndex = 1; }
        slides[slideIndex - 1].style.display = "block";
        setTimeout(showSlides, 2500); // Change d'image toutes les 3 secondes
    }

    showSlides();
});
