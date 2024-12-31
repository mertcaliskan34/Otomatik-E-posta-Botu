document.addEventListener("DOMContentLoaded", function () {
    
    document.querySelectorAll('.alert').forEach(alert => {
        alert.classList.add('fade-out');
        alert.addEventListener('animationend', () => alert.remove(), { once: true });
    });

    const generateReplyButton = document.getElementById('generateReplyButton');
    const generatedReply = document.getElementById('generatedReply');

    generateReplyButton.addEventListener('click', function () {
        const emailContent = document.getElementById('emailContent').value;

        fetch('/generate-reply/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ emailContent: emailContent })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP Error: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    generatedReply.value = data.reply; // Gelen yanıtı textarea'ya yaz
                } else {
                    alert(data.error || 'Yanıt oluşturulurken bir hata oluştu.');
                }
            })
            .catch(error => {
                console.error('Hata:', error);
                alert('Bir hata oluştu.');
            });
    });

    function getCsrfToken() {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'csrftoken') {
                return value;
            }
        }
        return null;
    }
});