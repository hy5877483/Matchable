from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def login_view(request) :
    if request.method == 'POST' :
        id = request.POST['id']
        pw = request.POST['pw']
        user = authenticate(request, username = id, password = pw)
        if user is not None :
            login(request, user)
            return redirect('main')
        else :
            return redirect('login')
    return render(request, 'account/login.html')

def logout_view(request) :
    logout(request)
    return redirect('main')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        id = request.POST['id']
        pw_1 = request.POST['pw_1']
        pw_2 = request.POST['pw_2']
        if pw_1 == pw_2 :
            return redirect('signup')
        else :
            try :
                user = User.objects.get(username = id)
                return redirect('signup')
            except ObjectDoesNotExist :
                user = User.objects.create_user(email = email, username = id, password = pw_1)
                login(request, user)
                return redirect('main')
    return render(request, 'account/signup.html')
