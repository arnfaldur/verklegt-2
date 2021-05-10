from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from user.forms import ProfileForm, UserRegistrationForm
from user.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def userprofile(request):
    profile = User.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/userprofile.html', {
        'form': ProfileForm(instance=profile)
    })

