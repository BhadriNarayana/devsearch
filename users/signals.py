from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender = User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )


@receiver(post_delete, sender = Profile)
def deleteUser(sender, instance, created, **kwargs):
    user = instance.user
    user.delete()



@receiver()
def updateUser(sender, instance, created, **kwargs):
    return

""" 
post_save.connect(createProfile, sender = User)
post_delete.connect(deleteUser, sender = Profile) """