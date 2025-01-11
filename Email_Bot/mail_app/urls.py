from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    
    path('inbox-page/', views.inboxpage, name="inbox_page"),
    
    path('inbox-page/<str:email_id>/', views.email_details, name="email_details"),
    
    path('reply-page/<str:email_id>/', views.reply_page, name="reply_page"),
    
    path('send-reply/<str:email_id>/', views.send_reply, name="send_reply"),
    
    path('fast-reply/', views.fast_reply, name="fast_reply"),
    
    path('google-login/', views.google_login, name="google_login"),
    
    path('logout/', views.google_logout, name="logout"),
    
    path('generate-reply/', views.generate_reply, name="generate_reply")
]