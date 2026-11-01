document.addEventListener("DOMContentLoaded", () => {
    if (document.querySelector(".md-typeset h1")) {
        const button = document.createElement("button");

        button.textContent = "↓ EXPORT PDF";
        button.className = "pdf-button";
        button.onclick = () => window.print();

        document.querySelector(".md-content__inner").prepend(button);
    }
});
