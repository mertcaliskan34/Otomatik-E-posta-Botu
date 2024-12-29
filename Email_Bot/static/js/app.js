document.addEventListener("DOMContentLoaded", function () {
    const alerts = document.querySelectorAll('.alert');
    const alertCloseButtons = document.querySelectorAll('.btn-close');
    const replyForm = document.querySelector('form');
    const emailContentInput = document.getElementById('emailContent');
    const generatedReply = document.getElementById('generatedReply');

    const fadeOutAlert = (alert) => {
        alert.classList.add('fade-out'); // Fade-out animasyonu başlat
        alert.addEventListener('animationend', () => {
            alert.remove(); // Tamamen DOM'dan kaldır
        }, { once: true });
    };

    const showError = (message) => {
        const errorMessageDiv = document.getElementById('errorMessage');
        if (errorMessageDiv) {
            errorMessageDiv.textContent = message;
            errorMessageDiv.classList.remove('d-none'); // Görünür yap
            errorMessageDiv.classList.add('show'); // Bootstrap animasyonu
            fadeOutAlert(errorMessageDiv); // Fade-out animasyonu başlat
        }
    };

    const initializeAlerts = () => {
        alerts.forEach(alert => fadeOutAlert(alert));
    };

    const initializeAlertCloseButtons = () => {
        alertCloseButtons.forEach(button => {
            button.addEventListener('click', () => {
                const alertBox = button.closest('.alert');
                if (alertBox) {
                    fadeOutAlert(alertBox); // Fade-out animasyonu başlat
                }
            });
        });
    };

    const initializeReplyFormValidation = () => {
        if (replyForm && generatedReply) {
            replyForm.addEventListener('submit', function (event) {
                if (!generatedReply.value.trim()) {
                    event.preventDefault(); // Form gönderimini engelle
                    showError('Yanıt içeriği boş olamaz.');
                }
            });
        }
    };

    const initializeApp = () => {
        initializeAlerts();
        initializeAlertCloseButtons();
        initializeReplyFormValidation();
    };

    initializeApp();
});