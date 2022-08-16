from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='users/%Y/%m/%d')


