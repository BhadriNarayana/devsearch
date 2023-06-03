from django.shortcuts import render
from .models import Profile

# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles':profiles})


def userProfile(request, pk):
    profile = Profile.objects.get(id = pk)

    topSkills = Profile.skill_set.exclude(description__exact = "")
    otherSkills
    return render(request, 'users/user-profile.html', {'profile':profile})
    

