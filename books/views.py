import os
from django.conf import settings
from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser
from rest_framework import views
from .models import Book
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import BookNameSerializer, UploadBookSerializer

# Create your views here.


class FileUploadView(views.APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        try:
            file_serializer = UploadBookSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                return Response(file_serializer.data, status=200)
            else:
                return Response(file_serializer.errors, status=500)
        except Exception as e:
            return Response('Could not be Processed. Reasons' + e, status=500)


class GetBooksList(views.APIView):
    def get(self, request):
        try:
            books = Book.objects.all()
            serializer = BookNameSerializer(books, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response('Could not be processed. Reasons:' + e, status=500)


class DownloadBooks(views.APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        path = request.GET.get('file')
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response

