import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .gmail_api import gmail_authenticate, list_messages
from .gmail_api import is_user_authenticated, get_email_details
from django.contrib import messages

def homepage(request):
    if is_user_authenticated():
        request.session['gmail_authenticated'] = True
    else:
        request.session['gmail_authenticated'] = False
    return render(request, 'mail_app/anasayfa.html')

def google_login(request):
    try:
        service = gmail_authenticate()
        request.session['gmail_authenticated'] = True
        messages.success(request, "Başarıyla giriş yaptınız.")
        return redirect('gelen_kutusu')
    except Exception as e:
        return HttpResponse(f"Bir hata oluştu: {e}")
    
def google_logout(request):
    token_path = 'token.pickle'
    if os.path.exists(token_path):
        os.remove(token_path)
        request.session['gmail_authenticated'] = False
        messages.success(request, "Başarıyla çıkış yaptınız.")

    return redirect('')

def inboxpage(request):
    if not is_user_authenticated():
        messages.warning(request, "Lütfen önce Gmail ile giriş yapın.")
        return redirect('google_login')
    
    service = gmail_authenticate()
    emails = list_messages(service)
    return render(request, 'mail_app/gelen_kutusu.html', {'emails': emails})

def email_details(request, email_id):
    try:
        service = gmail_authenticate()
        email = get_email_details(service, email_id)
        return render(request, 'mail_app/email_details.html', {'email': email})
    except Exception as e:
        return HttpResponse(f"Bir hata oluştu: {e}")