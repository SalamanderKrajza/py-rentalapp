from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .forms import MyUserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #It saves date inside database (creating new user) and returns created user
            #log the user in
            login(request, user)
            return redirect('/')
    else:
        form = MyUserCreationForm()

    #Returns unvalid form if method=POST or empty one if method=GET  
    stuff_for_frontend = {'form':form}
    return render(request, 'accounts/signup.html', stuff_for_frontend)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #Log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('blogapp:article_list')
    else:
        form = AuthenticationForm()

    #Returns unvalid form if method=POST or empty one if method=GET  
    stuff_for_frontend = {'form':form}
    return render(request, 'accounts/login.html', stuff_for_frontend)
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blogapp:article_list')