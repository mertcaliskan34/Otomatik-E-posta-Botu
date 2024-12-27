from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    
    path('gelen_kutusu/', views.inboxpage, name="gelen_kutusu"),
    
    path('gelen-kutusu/<str:email_id>/', views.email_details, name="email_details"),
    
    path('reply/<str:email_id>/', views.reply_page, name="reply_page"),
    
    path('google-login/', views.google_login, name="google_login"),
    
    path('logout/', views.google_logout, name="logout"),

    path('generate-reply/', views.generate_reply, name='generate_reply'),
]