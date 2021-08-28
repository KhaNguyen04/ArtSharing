from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account '+username+' created successfully!')
            return redirect('user-created')
    context={'form':form}
    return render(request,'accounts/SignUp.html',context)

def loginApp(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('web-home')
        else:
            messages.info(request,'Username or Password is incorrect')
    context={}
    return render(request,'accounts/LogIn.html', context)

def logoutApp(request):
    logout(request)
    return redirect('web-login')

def usercreated(request):
    return render(request,'accounts/UserCreated.html')