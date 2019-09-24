from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.book_name

