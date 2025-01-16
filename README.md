## Proje Başlığı

CleverRespond Otomatik Cevaplama E-posta Botu 

## Proje Amacı

Bu projenin amacı gelen e-postaları analiz ederek uygun yanıtları öneren bir otomatik yanıt sistemi oluşturmaktır. Bu sistem hem zamandan tasarruf sağlayacak hem de müşteri memnuniyetini arttıracaktır.

## Kullanılan Teknolojiler

#### Django Framework:
Projenin bir web sayfası üzerinde yer alması uygun görülmüş, kullanıcı arayüzünün kurulması ve backend işlevlerinin yazımı için Django Framework teknolojisi üzerinde uzlaşılmıştır.
#### HTML, CSS, Bootstrap ve JavaScript:
Projenin frontend kısmının tasarımı için HTML, CSS, Bootstrap ve JavaScript teknolojileri kullanılmıştır.
#### Doğal Dil İşleme (NLP) Modeli:
Doğal Dil İşleme (NLP) modeli kullanılarak e-posta metinleri analiz edilebilmekte ve bu metinlere uygun yanıtlar üretilebilmektedir. Bunu mümkün kılmak için Meta tarafından geliştirilen Llama 3 modeli kullanılmaktadır.
#### Kütüphaneler:
Python dilinin içerisinde yer alan birçok kütüphane bu proje içerisinde kullanılmaktadır. Söz konusu kütüphaneler proje dizininde yer alan 'requirements.txt' dosyasında belirtilmiştir.
#### E-posta Servisi Entegrasyonu:
Gmail API kullanılarak botun e-posta alışverişini gerçekleştirmesi sağlanmıştır.

## Proje Özellikleri

#### E-posta Okuma:
Gmail API bağlantısı sayesinde kullanıcının son e-postalarını listeleme ve istenen e-postayı detaylarıyla görüntüleyebilme.
#### Konu Analizi:
Cevap oluşturulurken e-postaların ana konularını (sipariş, iade, bilgi talebi vb.) belirleyebilme.
#### Duygu Analizi:
Müşterinin e-posta içeriğindeki duygu durumunu (olumlu, olumsuz) belirleyip uygun bir üslup seçebilme.
#### Yanıt Oluşturma:
Doğal dil işleme modelini kullanarak konu ve duygu analizleri yaptıktan sonra e-postaya yanıt oluşturabilme.
#### Hızlı Yanıt Oluşturma Sayfası:
Gmail ile giriş yapmak istemeyen kullanıcılar için oluşturulmuş bir sayfada istenilen e-postaya anında uygun bir cevap üretebilme.
#### E-posta Gönderme:
Gmail API bağlantısı sayesinde kullanıcının oluşturduğu yanıtı e-postayı gönderen kişinin adresine gönderebilme.

## Aşamalar

#### UI Tasarımı:
Django ile kullanımı kolay, anlaşılabilir bir kullanıcı arayüzü geliştirme.
#### API Entegrasyonu ve Veri Toplama:
Projeye uygun verilerin toplanabilmesi için Gmail API bağlantısının kurulması, sonrasında toplanan verilerin kullanıcı arayüzünde listelenmesi.
#### Model Seçimi:
Llama 3 NLP modelinin seçilmesi ve kullanılmaya başlanması.
#### Yanıt Şablonunun Hazırlanması:
E-postalara olması gereken formatta ve doğru yapıda yanıt üretilebilmesini sağlamak için modele verilen promptların geliştirilmesi.
#### Test ve Geliştirme:
Geliştiricilerin Gmail hesapları üzerinden test işlemlerinin yapılması ve eğer gerekliyse yanıt oluşturma işlevlerinin geliştirilmesi.
