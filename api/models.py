from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CHOICES = [
        ('user', 'user'),
        ('admin', 'admin'),
        ('moderator', 'moderator'),
    ]

    conf_code = models.CharField(max_length=100, null=True, default=None)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    role = models.CharField(max_length=50, choices=CHOICES, default=CHOICES[0][0])
    password = models.CharField(max_length=30, blank=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ('username',)


