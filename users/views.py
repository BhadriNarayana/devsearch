from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomCreationForm, SkillForm

from .forms import ProfileForm
# Create your views here.

def profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    print()    

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
            return redirect('edit-account')
        
        else:
            messages.success(request, 'Error occured during registration')

    return render(request, 'users/login_register.html', {'page':page, 'form':form})



@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    
    return render(request, 'users/account.html', {'profile':profile, 'skills':skills, 'projects':projects})



@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        #try:
        if form.is_valid():
            form.save()
            return redirect('account')
        """ else:
            messages.success(request, 'Error occured during registration') """
        #except:
        #messages.error(request, "Error occured")
    return render(request, 'users/profile_form.html', {'form':form})



@login_required(login_url= 'login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit = False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill was added successfully!")
            return redirect('account')

    return render(request, 'users/skill_form.html', {'form':form})



@login_required(login_url= 'login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    form = SkillForm(instance = skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance = skill)

        if form.is_valid():
            form.save()
            messages.success(request, "Skill was updated successfully!")
            return redirect('account')
        
    return render(request, 'users/skill_form.html', {'form':form})



login_required()
def deleteSkill(request, pk):
    page = 'skill'
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')

    return render(request, 'delete-object.html', {'object':skill})

