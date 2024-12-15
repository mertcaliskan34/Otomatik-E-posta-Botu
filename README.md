## Proje Başlığı

Otomatik E-posta Botu

## Proje Amacı

Bu projenin amacı gelen e-postaları analiz ederek uygun yanıtları öneren bir otomatik yanıt sistemi oluşturmaktır. Bu sistem hem zamandan tasarruf sağlayacak hem de müşteri memnuniyetini arttıracaktır.

## Kullanılacak Teknolojiler

#### NLP Modelleri:
Doğal Dil İşleme (NLP) kullanarak e-posta metinlerini analiz etme ve doğru yanıtları önerme.
#### Kütüphaneler:
Python (google-api-python-client, google-auth-httplib2, google-auth-oauthlib, django).
#### Veritabanı:
SQLite3, e-posta içerikleri ve geri bildirimleri depolamak için kullanılacak.
#### E-posta Servisi Entegrasyonu:
Gmail API ile botun e-posta alışverişini sağlayacak entegrasyon.

## Proje Özellikleri

#### Konu Analizi:
E-postaların ana konularını (sipariş, iade, bilgi talebi vb.) belirleme.
#### Duygu Analizi:
Müşterinin e-posta içeriğindeki duygu durumunu (olumlu, olumsuz) belirleyip uygun bir üslup seçme.
#### Yanıt Şablonları:
Hazır yanıt şablonları kullanarak kullanıcıya hızlı yanıt önerileri sunma.
#### Otomatik Öğrenme:
Geri bildirimlerle yanıt önerilerini iyileştirme.

## Aşamalar

#### Veri Toplama:
Projeye uygun verilerin toplanması ve ön işlenmesi.
#### Model Seçimi ve Eğitimi:
NLP modeliyle metin analizleri ve duygu analizi sağlama.
#### Yanıt Şablonlarının Hazırlanması:
Sıkça sorulan sorulara uygun yanıt şablonları belirleme.
#### API Geliştirme ve Entegrasyon:
E-posta servisleriyle entegrasyon ve kullanıcı arayüzü geliştirme.
#### Geri Bildirim ve Öğrenme:
Kullanıcı geri bildirimlerini analiz ederek sistemin iyileştirilmesi.

İndirilen bu dosya proje dizinine koyulmalı, ismi 'client_secret' yapılmalı ve sonrasında create_service.py dosyası çalıştırılarak Gmail API Authentication işlemi yapılmalıdır. Bu işlemden sonra proje dizininde 'token files' isminde bir dosya oluşacaktır. Artık basitçe read_emails.py dosyasını çalıştırabilir ve istediğiniz parametrelere uygun bir şekilde e-postalarınızı görüntüleyebilirsiniz.

Not: Gmail API sadece sonu 'gmail.com' ile biten e-posta adresleri için çalışmaktadır.
