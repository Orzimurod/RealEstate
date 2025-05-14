from django.urls import path
from login.views import login_user, register_user

urlpatterns = [
    path('', login_user, name='login'),
    path('register/', register_user, name='register')
]