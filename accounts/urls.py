from django.conf.urls import url, include
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('create-user/', views.CreateUserView.as_view(), name='create-user'),
    path('reset-password', views.ResetPasswordView.as_view(), name='reset-password'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
