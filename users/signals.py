from django.db.models.signals import post_save
from .models import Profile


def profileUpdated(sender, instance, created, **kwargs):
    print("profile saved!")
    print("Sender:", sender)
    print("Created", created)

post_save.connect(profileUpdated, sender = Profile)