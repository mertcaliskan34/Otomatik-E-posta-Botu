document.addEventListener('DOMContentLoaded', function () {
    const generateReplyButton = document.getElementById('generateReplyButton');
    const emailContent = document.getElementById('emailContent').value;
    const generatedReply = document.getElementById('generatedReply');

    generateReplyButton.addEventListener('click', function () {
        // Sunucuya AJAX ile istek gönder
        fetch('/generate-reply/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ emailContent: emailContent })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    generatedReply.value = data.reply; // Gelen yanıtı textarea'ya yaz
                } else {
                    alert('Yanıt oluşturulurken bir hata oluştu.');
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
