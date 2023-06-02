from django.db import models
from django.contrib
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 200, blank = True, null = True)
    email = models.EmailField(max_length = 500, blank = True, null = True)
    short_intro = models.CharField(max_length = 200, blank = True, null = True)
    bio = models.TextField(blank = True, null = True)
    profile_image = models.ImageField(null = True, blank = True, upload_to = 'profiles/', default='profiles/default.png')
    social_twitter = models.CharField(max_length = 200, blank=True, null = True)
    social_github = models.CharField(max_length = 200, blank=True, null = True)
