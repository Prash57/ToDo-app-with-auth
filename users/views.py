import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'users/home.html')


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('list')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list')
    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('index')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User Registered')

            login(request, user)
            return redirect('list')

        else:
            messages.error(request, 'User not registered')

    context = {'page': page, 'form': form}
    return render(request, 'users/register.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def deleteProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully')
        return redirect('home')

    context = {'object': profile}
    return render(request, 'users/delete_profile.html', context)
