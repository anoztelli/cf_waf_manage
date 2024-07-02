from django.contrib import admin
from django.urls import path
from main import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), # Çıkış URL'sini tanımla
    path('secret/', views.secret_view, name='secret'),
]
