from django.shortcuts import render , redirect
from django.contrib.auth import logout
def home(request):
    return render(request , 'index.html')


def custom_logout(request):
    logout(request)
    return redirect('post-list')