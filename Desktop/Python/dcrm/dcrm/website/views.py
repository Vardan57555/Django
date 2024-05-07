from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
     if request.method == 'POST':
        
        username1 = request.POST['username'],
        password = request.POST['password']
        username = username1[0]
        print(username)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
          print(user)
          login(request, user)
          messages.success(request, 'You have been Logged In!')
          return redirect('home')
        else:
          messages.success(request, "There was an error Logging In, Please Try Again")
          return redirect('home')
     else:
         return render(request,'home.html', {}) 



def login_user(request):
     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('home')

def register(request):
    return render(request, 'register.html')