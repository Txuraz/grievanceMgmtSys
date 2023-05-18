from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        full_name = request.POST.get['full_name']
        email = request.POST.get['email']
        password = request.POST.get['password']

        myuser = User.objects.create_user(full_name, email, password)
        myuser.full_name = full_name

        myuser.save()

        messages.success(request, "Account Created Successfully!")

        return render(request, 'home')
    return render(request, 'home')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request,user)

        else:
            messages.error(request, 'Incorrect Email or Password.')
            return render(request, 'home')
        return render(request, 'home')
