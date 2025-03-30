# CleverRespond: Yapay Zeka Destekli E-posta Otomasyonu

## Genel Bakış

CleverRespond, e-posta yönetimini ve yanıt oluşturmayı kolaylaştırmak için tasarlanmış akıllı bir e-posta otomasyon aracıdır. Yapay zekanın gücünden yararlanarak gelen e-postaları analiz eder, bağlamlarını ve duygusal tonlarını anlar ve uygun yanıtlar oluşturur. Bu sayede zaman tasarrufu sağlar ve müşteri memnuniyetini artırır.

## Temel Özellikler

- **Akıllı E-posta Analizi:** Gelen e-postaları otomatik olarak okur ve analiz eder.
- **Duygu Analizi:** E-postaların duygusal tonunu (pozitif, negatif, nötr) algılayarak yanıtları buna göre uyarlar.
- **Yapay Zeka Destekli Yanıt Oluşturma:** Meta tarafından geliştirilen Llama 3 NLP modelini kullanarak bağlamsal olarak uygun ve kişiselleştirilmiş e-posta yanıtları üretir.
- **Hızlı Yanıt Arayüzü:** Gmail girişi gerektirmeden hızlı yanıtlar oluşturmak için bir arayüz sunar.
- **Gmail Entegrasyonu:** Gmail API aracılığıyla güvenli ve verimli e-posta yönetimi sağlar.
- **E-posta Listeleme ve Detayları:** Son e-postaları önemli detaylarla listeler ve kullanıcıların tam e-posta içeriğini görüntülemesine olanak tanır.
- **Otomatik E-posta Gönderimi:** Oluşturulan yanıtları doğrudan Gmail API üzerinden gönderir.

## Kullanılan Teknolojiler

**Backend:**

- Django Framework
- Python
- Gmail API
- Langchain
- Ollama
- TextBlob
- Deep Translator

**Frontend:**

- HTML
- CSS
- Bootstrap
- JavaScript

## Kurulum Talimatları

1. **Depoyu klonlayın:**

    ```bash
    git clone [depo URL'si]
    cd CleverRespond
    ```

2. **Sanal bir ortam oluşturun:**

    ```bash
    python -m venv venv
    ```

3. **Sanal ortamı etkinleştirin:**

    - **Windows'ta:**

        ```bash
        .\venv\Scripts\activate
        ```

    - **macOS ve Linux'ta:**

        ```bash
        source venv/bin/activate
        ```

4. **Bağımlılıkları yükleyin:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Gmail API kimlik bilgilerini ayarlayın:**

    - Gmail API dokümantasyonundaki talimatları izleyerek bir proje oluşturun ve `credentials.json` dosyanızı indirin.
    - `credentials.json` dosyasını projenin ana dizinine yerleştirin.

6. **Veritabanı migrasyonlarını çalıştırın:**

    ```bash
    python manage.py migrate
    ```

7. **Geliştirme sunucusunu başlatın:**

    ```bash
    python manage.py runserver
    ```

8. **Uygulamaya tarayıcınızdan erişin:**

    Web tarayıcınızı açın ve `http://localhost:8000` adresine gidin.

## Kullanım

1. **Gmail Kimlik Doğrulaması:**
    - Ana sayfada, Google hesabınızla kimlik doğrulaması yapmak için "Gmail ile Giriş Yap" düğmesine tıklayın.
2. **Gelen Kutusu:**
    - Başarılı bir kimlik doğrulamasından sonra, "Gelen Kutusu" bölümüne giderek e-postalarınızı görüntüleyin.
3. **E-posta Detayları:**
    - Bir e-postanın tam içeriğini ve detaylarını görüntülemek için "Detaylar" düğmesine tıklayın.
4. **Yanıt Oluştur:**
    - E-posta için yapay zeka destekli bir yanıt oluşturmak üzere "Yanıt Oluştur" düğmesine tıklayın.
5. **Hızlı Yanıt:**
    - Gmail ile kimlik doğrulaması yapmadan yanıtlar oluşturmak için "Hızlı Yanıt Oluştur" özelliğini kullanın.
6. **Yanıtı Gönder:**
    - Oluşturulan yanıtı gözden geçirin ve "Yanıtı Gönder" düğmesine tıklayarak e-postayı gönderin.
