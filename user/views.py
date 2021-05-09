from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

def userprofile(userprofile):
        return render(userprofile, 'user/userprofile.html')

