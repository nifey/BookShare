from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    published_date = models.DateField()
    file = models.FileField(blank=False, null=False, default=None)

    def __str__(self):
        return self.book_name


class Rating(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    stars = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.book) + '_' + str(self.stars)


class Review(models.Model):
    user = models.ForeignKey('accounts.user', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.book) + '_' + str(self.review)

