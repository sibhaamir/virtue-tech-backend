from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # You can add extra fields later
    pass
firebase_uid = models.CharField(max_length=200, unique=True, null=True, blank=True)
avatar = models.URLField(null=True, blank=True)
