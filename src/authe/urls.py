from django.urls import path, include
from .views import register, confirm_email, login, logout_view

app_name = 'authe'

urlpatterns = [
    path('register/', register, name = 'register'),
    path('confirm/<str:code>', confirm_email, name = 'confirm'),
    path('log_in/', login, name='login'),
    path('log_out/', logout_view, name = 'logout'),
]