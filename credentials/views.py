from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=username, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid User")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=pwd)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password not matching")
            return redirect('register')

        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
