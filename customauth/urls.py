from django.urls import path, include
from .views import login_user, register_user, home

urlpatterns = [
    path('', home, name='Home'),
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
]