document.addEventListener("DOMContentLoaded", function () {
    // DOM Elemanlarını Başlat
    const alerts = document.querySelectorAll('.alert');
    const alertCloseButtons = document.querySelectorAll('.btn-close');
    const replyButtons = document.querySelectorAll(".reply-button");
    const emailContentInput = document.getElementById('emailContent');

    // Fade Out Animasyonu (Helper Fonksiyon)
    const fadeOutAlert = (alert, delay = 20000) => {
        setTimeout(() => {
            alert.classList.add('fade-out');
            alert.addEventListener('transitionend', () => {
                alert.style.display = 'none';
            }, { once: true });
        }, delay);
    };

    // Hata Mesajı Gösterme (Helper Fonksiyon)
    const showError = (message) => {
        const errorMessageDiv = document.getElementById('errorMessage');
        if (errorMessageDiv) {
            errorMessageDiv.textContent = message;
            errorMessageDiv.classList.remove('d-none'); // Görünür yap
            errorMessageDiv.classList.add('show'); // Bootstrap için animasyonlu görünüm
            setTimeout(() => {
                errorMessageDiv.classList.remove('show');
                errorMessageDiv.classList.add('d-none'); // 5 saniye sonra gizle
            }, 5000);
        }
    };

    // Tüm Alertler için Fade-Out Uygula
    alerts.forEach(alert => fadeOutAlert(alert));

    // Alert Kapatma Düğmeleri
    alertCloseButtons.forEach(button => {
        button.addEventListener('click', () => {
            const alertBox = button.closest('.alert');
            if (alertBox) {
                alertBox.classList.remove('show');
                alertBox.classList.add('fade');
            }
        });
    });
});