from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('auth/login/', LoginAPIView.as_view(), name= "login"),
    path('auth/logout/', LogoutAPIView.as_view(), name='logout'),
    path('user/', UserAPIView.as_view(), name='user'),
]
