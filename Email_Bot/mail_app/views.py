import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .gmail_api import gmail_authenticate, list_messages, is_user_authenticated
from .gmail_api import get_email_details, send_email
from django.contrib import messages
import json
import re
from .email_generator import generate_llama
from django.views.decorators.http import require_POST
import logging

# Yardımcı Fonksiyon: Gmail Doğrulama
def get_authenticated_service():
    try:
        return gmail_authenticate()
    except Exception as e:
        return None

# Anasayfa Görüntüleme
def homepage(request):
    request.session['gmail_authenticated'] = is_user_authenticated()
    return render(request, 'mail_app/anasayfa.html')

# Gmail Giriş İşlemi
def google_login(request):
    try:
        service = gmail_authenticate()
        request.session['gmail_authenticated'] = True
        messages.success(request, "Başarıyla giriş yaptınız.")
        return redirect('gelen_kutusu')
    except Exception as e:
        messages.error(request, f"Bir hata oluştu: {e}")
        return redirect('')

# Gmail Çıkış İşlemi
def google_logout(request):
    token_path = 'token.pickle'
    if os.path.exists(token_path):
        os.remove(token_path)
        request.session['gmail_authenticated'] = False
        messages.success(request, "Başarıyla çıkış yaptınız.")
    return redirect('')

# Gelen Kutusu Sayfası
def inboxpage(request):
    if not is_user_authenticated():
        messages.warning(request, "Lütfen önce Gmail ile giriş yapın.")
        return redirect('google_login')
    
    service = get_authenticated_service()
    if not service:
        messages.error(request, "Gmail hizmetine bağlanılamadı.")
        return redirect('')

    emails = list_messages(service)
    return render(request, 'mail_app/gelen_kutusu.html', {'emails': emails})

# E-posta Detayları
def email_details(request, email_id):
    try:
        service = get_authenticated_service()
        if not service:
            raise Exception("Gmail hizmetine bağlanılamadı.")
        
        email = get_email_details(service, email_id)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(email)
        return render(request, 'mail_app/email_details.html', {'email': email})
    except Exception as e:
        return HttpResponse(f"Bir hata oluştu: {e}")

# E-posta Yanıtlama Sayfası
def reply_page(request, email_id):
    try:
        service = get_authenticated_service()
        if not service:
            messages.error(request, "Gmail hizmetine bağlanılamadı.")
            return redirect('gelen_kutusu')

        email = get_email_details(service, email_id)
        return render(request, 'mail_app/reply.html', {'email': email})
    except Exception as e:
        messages.error(request, f"Bir hata oluştu: {e}")
        return redirect('gelen_kutusu')

# Hızlı Yanıt Sayfası
def fast_reply(request):
    return render(request, 'mail_app/fast_reply.html')

# E-posta Adresini Ayıklama
def extract_email_address(email_string):
    """
    E-posta adresini metinden ayıkla.
    Örn: 'John Doe <john.doe@example.com>' -> 'john.doe@example.com'
    """
    match = re.search(r'[\w\.-]+@[\w\.-]+', email_string)
    return match.group(0) if match else email_string

# Yanıt Gönderme İşlemi
def send_reply(request, email_id):
    service = gmail_authenticate()
    email = get_email_details(service, email_id)

    if not email:
        messages.error(request, 'E-posta bilgileri alınamadı.')
        return redirect('gelen_kutusu')

    print(f"E-posta Detayları: {email}")  # DEBUG

    if request.method == 'POST':
        reply_content = request.POST.get('generatedReply')
        print(f"Oluşturulan Yanıt: {reply_content}")  # DEBUG

        if reply_content:
            to_address = extract_email_address(email['from'])  # E-posta adresini ayıkla
            try:
                send_email(service, to_address, f"Re: {email['subject']}", reply_content)
                messages.success(request, 'Yanıt başarılı bir şekilde gönderildi.')
                return redirect('gelen_kutusu')
            except Exception as e:
                print(f"Email gönderim hatası: {e}")  # DEBUG
                messages.error(request, f'Bir hata oluştu: {e}')
        else:
            messages.error(request, 'Yanıt içeriği boş olamaz.')

    return render(request, 'mail_app/reply.html', {'email': email})

# Yanıt Oluşturma API
logger = logging.getLogger(__name__)

@require_POST
def generate_reply(request):
    try:
        # Gelen POST verisini JSON olarak yükle
        data = json.loads(request.body)
        logger.debug(f"Received request body: {data}")

        # Veri tipini kontrol et: Verinin bir dict (sözlük) olup olmadığını kontrol et
        if not isinstance(data, dict):
            return JsonResponse({'success': False, 'error': 'Expected JSON object, but received a different format'}, status=400)

        email_text = data.get('emailContent')
        
        # emailContent alanı zorunlu
        if not email_text:
            return JsonResponse({'success': False, 'error': 'emailContent is required'}, status=400)

        # Yanıt oluştur
        reply = generate_llama(email_text)
        return JsonResponse({'success': True, 'reply': reply})

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return JsonResponse({'success': False, 'error': 'Internal server error'}, status=500)