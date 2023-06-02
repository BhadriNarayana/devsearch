from django.db import models
from django.contrib
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 200, blank = True, null = True)
    email = models.EmailField(max_length = 500, blank = True, null = True)