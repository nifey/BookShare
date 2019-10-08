from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from .models import Book
from rest_framework.response import Response
from .serializers import BookNameSerializer
# Create your views here.


class GetBooksList(views.APIView):
    def get(self, request):
        try:
            books = Book.objects.all()
            serializer = BookNameSerializer(books, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response('Could not be processed', status=500)
