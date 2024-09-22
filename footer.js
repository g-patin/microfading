document.addEventListener("DOMContentLoaded", function() {
    const footer = document.querySelector("footer");
    if (footer) {
        const year = new Date().getFullYear();
        footer.innerHTML += `Gauthier Patin - Last updated in ${year}`;
        
        // Apply the white text color
        footer.style.color = 'white';
    }
});

