document.addEventListener("DOMContentLoaded", function () {
    // === DOM Elemanları ===
    const alerts = document.querySelectorAll('.alert');
    const alertCloseButtons = document.querySelectorAll('.btn-close');
    const replyForm = document.querySelector('form');
    const emailContentInput = document.getElementById('emailContent');
    const generatedReply = document.getElementById('generatedReply');

    // === Helper Fonksiyonlar ===

    // Fade Out Animasyonu
    const fadeOutAlert = (alert, delay = 20000) => {
        setTimeout(() => {
            alert.classList.add('fade-out');
            alert.addEventListener('transitionend', () => {
                alert.style.display = 'none';
            }, { once: true });
        }, delay);
    };

    // Hata Mesajı Gösterme
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

    // === İşlevler ===

    // Tüm Alertler için Fade-Out Uygula
    const initializeAlerts = () => {
        alerts.forEach(alert => fadeOutAlert(alert));
    };

    // Alert Kapatma Düğmeleri
    const initializeAlertCloseButtons = () => {
        alertCloseButtons.forEach(button => {
            button.addEventListener('click', () => {
                const alertBox = button.closest('.alert');
                if (alertBox) {
                    alertBox.classList.remove('show');
                    alertBox.classList.add('fade');
                }
            });
        });
    };

    // Form Doğrulama
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

    // === Başlatıcılar ===
    const initializeApp = () => {
        initializeAlerts();
        initializeAlertCloseButtons();
        initializeReplyFormValidation();
    };

    // Uygulamayı Başlat
    initializeApp();
});