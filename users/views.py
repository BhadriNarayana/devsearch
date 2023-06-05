from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

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
        print(username)
        print(password)

        try:
            user = User.objects.get(username = username)
        except:
            print("User does not exist")   

        user = authenticate(request, username = username, password = password)
        

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print("")

       
    return render(request, 'users/login_register.html')