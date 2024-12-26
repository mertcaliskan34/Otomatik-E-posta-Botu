import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .gmail_api import gmail_authenticate, list_messages, is_user_authenticated, get_email_details
from django.contrib import messages
import torch
import json

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