from .models import Book, Review
from rest_framework import serializers


class BookNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UploadBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
