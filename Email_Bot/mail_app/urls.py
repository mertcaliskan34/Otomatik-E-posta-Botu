from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.homepage, name=""),
    
    path('gelen_kutusu/', views.inboxpage, name="gelen_kutusu"),
    
    path('gelen-kutusu/<str:email_id>/', views.email_details, name='email_details'),
    
    path('google-login/', views.google_login, name="google_login"),
    
    path('logout/', views.google_logout, name="logout")
]
