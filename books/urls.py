from . import views
from django.urls import path

urlpatterns = [
    path('book-list/', views.GetBooksList.as_view(), name='book-list'),
    path('file-upload/', views.FileUploadView.as_view(), name='file-upload'),
    path('file-download/', views.DownloadBooks.as_view(), name='book-download')
]

