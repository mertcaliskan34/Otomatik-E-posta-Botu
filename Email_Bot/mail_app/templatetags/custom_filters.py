from django import template
import re
from django.utils.html import escape

register = template.Library()

@register.filter
def convert_links(value):
    # Önce gelen değeri olası kötü HTML'den temizle (escape)
    escaped_value = escape(value)
    
    # URL'leri tespit etmek için regex
    url_pattern = r'(https?://[^\s]+)'
    
    # URL'leri <a> etiketiyle değiştir
    return re.sub(
        url_pattern,
        '',
        escaped_value
    )