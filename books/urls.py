from . import views
from django.urls import path

urlpatterns = [
    path('book-list', views.GetBooksList.as_view(), name='book-list')
]
