from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(null=True, blank= True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username