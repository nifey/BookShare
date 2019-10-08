from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('create-user/', views.CreateUserView.as_view(), name='create-user')
]
