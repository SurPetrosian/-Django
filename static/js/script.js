// ==== Инициализация AOS.js ====
document.addEventListener("DOMContentLoaded", function () {
    if (AOS) {
        AOS.init({
            duration: 800,
            once: true,
        });
    }
});

// ==== Пример интерактива ====
console.log("🚗 Автоблог подключён!");

const footer = document.querySelector("footer");
if (footer) {
    footer.addEventListener("click", () => {
        alert("Спасибо, что читаете наш автоблог!");
    });
}
