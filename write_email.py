import os
from dotenv import load_dotenv
from openai import OpenAI, APIError, RateLimitError

# .env dosyasını yükle
load_dotenv()

# OpenAI istemcisini başlat
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    # Mesajlar ile sohbet isteği oluştur
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Hello!"}
        ]
    )
    # Yanıtı yazdır
    print(completion.choices[0].message.content)

except RateLimitError:
    print("API kotasını aştınız. Lütfen plan ve faturalandırma detaylarını kontrol edin.")
except APIError as e:
    print(f"OpenAI API hatası: {e}")
