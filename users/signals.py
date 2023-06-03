from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.dispatch import receiver

@receiver(post_save, sender = Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = created
        profile = Profile.objects


@receiver(post_delete, sender = Profile)
def deleteUser(sender, instance, created, **kwargs):
    print("Deleting user")






""" post_save.connect(profileUpdated, sender = Profile)
post_delete.connect(deleteUser, sender = Profile) """