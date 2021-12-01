from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            print('invalid user credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'registration.html')
