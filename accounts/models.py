from datetime import timezone, datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=254, null=True, blank=True)
    first_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    mobile = models.IntegerField(unique=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=datetime.now())
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

