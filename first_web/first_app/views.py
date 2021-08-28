from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
# Create your views here.

def home(request):
    return render(request,'first_app/FrontPage.html')

def drawing(request):
    return render(request,'first_app/Drawing.html')

def photo(request):
    return render(request,'first_app/Photo.html')

def comic(request):
    return render(request,'first_app/Comic.html')

