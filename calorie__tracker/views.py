from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.

#register user
def registerUser(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                if user is not None:
                    login(request, user)
                    return redirect('home')
        context = {'form':form}
        return render(request,'register.html',context)

#login user
def loginUser(request):
        if request.method == 'POST':
            username = request.POST('username')
            password = request.POST('password')
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or password is incorrect')
                return redirect('login')
        else:
            return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')

def home(request):
    return render(request,'home.html')