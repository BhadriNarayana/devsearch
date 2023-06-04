from django.shortcuts import render
from .models import Profile
from django.contrib.auth import login, authenticate
from .models import Profile
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles':profiles})


def userProfile(request, pk):
    profile = Profile.objects.get(id = pk)

    topSkills = profile.skill_set.exclude(description__exact = "")
    otherSkills = profile.skill_set.filter(description = "")
    return render(request, 'users/user-profile.html', {'profile':profile, 'topSkills':topSkills, 'otherSkills':otherSkills})
    

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
    return render(request, 'users/login_register.html', {})