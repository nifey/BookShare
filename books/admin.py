from django.contrib import admin
from .models import Book, Rating, Review

admin.site.register(Book)
admin.site.register(Rating)
admin.site.register(Review)
