document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.alert').forEach(alert => {
        alert.classList.add('fade-out');
        alert.addEventListener('animationend', () => alert.remove(), { once: true });
    });
});