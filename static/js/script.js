console.log("ChronoLux website loaded successfully");


// Small animation when page loads

document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".watch-card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";

        setTimeout(() => {

            card.style.transition = "0.5s";

            card.style.opacity = "1";
            card.style.transform = "translateY(0)";

        }, index * 100);

    });

});