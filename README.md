## Alternatif E-posta Botu Projesi

#### Farklılıklar:
1) Python simplegmail kütüphanesi kullanılmaktadır.

## Projeyi Çalıştırma Koşulları

#### Python ile Virtual Environment Oluşturmak ve Onu Aktifleştirmek:
1) python -m venv virtual_environment_name
2) .\venv\Scripts\activate
#### Gerekli Kütüphaneleri Yüklemek:
pip install simplegmail
#### Gmail API'yi Aktifleştirmek:
Google Cloud Console üzerinden APIs & Services sekmesine geçilerek Gmail API bulunmalı ve aktifleştirilmelidir.
#### Proje Oluşturmak ve Credentials Dosyasını İndirmek:
Google Cloud Console üzerinden yeni bir proje oluşturulmalı ve sonrasında Create Credentials sekmesinde OAuth 2.0 Client ID seçeneği seçilerek bir istemci credentials json dosyası oluşturulup sonrasında indirilmelidir.

İndirilen bu dosya proje dizinine koyulmalı, ismi 'client_secret' yapılmalı ve sonrasında read_emails.py dosyası çalıştırılarak Gmail API Authentication işlemi yapılmalıdır. Bu işlemden sonra gmail_token.json dosyası proje dizininde oluşturulacaktır, devamında tekrardan read_emails.py dosyası çalıştırıldığında belirtilen tarih aralığındaki e-postalar terminal ekranında görüntülenecektir.

Not: Gmail API sadece sonu "gmail.com" ile biten e-posta adresleri için çalışmaktadır.
