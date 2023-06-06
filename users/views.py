from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CustomCreationForm
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles':profiles})


def userProfile(request, pk):
    profile = Profile.objects.get(id = pk)

    topSkills = profile.skill_set.exclude(description__exact = "")
    otherSkills = profile.skill_set.filter(description = "")
    return render(request, 'users/user-profile.html', {'profile':profile, 'topSkills':topSkills, 'otherSkills':otherSkills})
    


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User does not exist")   

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is incorrect")
       
    return render(request, 'users/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect("login")


def registerUser(request):
    page = 'register'
    form = CustomCreationForm()

    if request.method == 'POST':
        form = CustomCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account created successfully!")

            login(request, user)
            return redirect('profiles')
        
        else:
            messages.success(request, 'Error occured during registration')

    return render(request, 'users/login_register.html', {'page':page, 'form':form})


def editAccount(request):
    