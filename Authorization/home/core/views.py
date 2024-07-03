from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate,login,logout

#this is for sign_up
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "Form submitted successfully.")
            form.save()
            # return render(request, 'enroll.html')  # or redirect to another page
    else:
        form = SignUpForm()      
    return render(request, 'enroll.html', {'form': form})
def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/profile/')
            else:
                form.add_error(None, "Invalid username or password.")  # Display error if authentication fails
    return render(request, 'login.html', {'form': form})


def userProfile(request):
    return render(request,'profile.html')
