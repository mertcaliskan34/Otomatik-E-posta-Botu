document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".yanit_olustur");
    
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const emailId = button.getAttribute("data-id");
            alert(`#${emailId} numaralı e-posta için bir yanıt oluştur.`);
            // Burada bir API çağrısı ya da başka bir işlem yapabilirsin
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const alerts = document.querySelectorAll('.alert'); // Tüm alert mesajlarını seç
    
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.add('fade-out'); // Fade-out animasyonunu ekle
            setTimeout(() => {
                alert.style.display = 'none'; // Animasyon bitince tamamen gizle
            }, 20000); // 20 saniye sonra tamamen kaldır
        }, 0); // Hemen çalıştır
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Bootstrap alert'i kapatma işlemi
    var closeButtons = document.querySelectorAll('.btn-close');
    closeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var alertBox = button.closest('.alert');
            alertBox.classList.remove('show');
            alertBox.classList.add('fade');
        });
    });
});