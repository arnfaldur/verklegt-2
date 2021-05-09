from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import User
from user.forms.profile_form import ProfileForm



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

def userprofile(request):
    profile = User.objects.filter(name=request.user).first()
    if request. method == 'POST':
        print(1)
    return render(request, 'user/userprofile.html',{
        'form': ProfileForm()
    })

