from django import template
import re
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def clean_email_body(value):
    """
    Email body içindeki HTML kodlarını ve URL'leri temizler,
    yalnızca anlamlı metni döner.
    """
    # HTML'i temizlemek için BeautifulSoup kullanıyoruz
    soup = BeautifulSoup(value, "html.parser")
    
    # HTML etiketlerini kaldır
    cleaned_text = soup.get_text(separator=" ")
    
    # URL'leri kaldır
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    cleaned_text = re.sub(url_pattern, '', cleaned_text)
    
    # Gereksiz boşlukları temizle
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    # "[ Virus-free." ifadesini boş bir stringle değiştir
    cleaned_text = re.sub(r'\[ Virus-free\.', '', cleaned_text)
    
    return cleaned_text