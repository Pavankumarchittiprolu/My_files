from django.shortcuts import render
from app1.models import Users
from django.db.models import *

# Create your views here.
def home(request):
    response=render(request,'app1/home.html')
    return response

def signin(request):
    response=render(request,'app1/signin.html')
    return response

def signup(request):
    response=render(request,'app1/signup.html')
    return response

def welcome(request):
    response=render(request,'app1/welcome.html')
    return response

def change_password(request):
    response=render(request,'app1/change_password.html')
    return response

def signup_view(request):
    name=request.GET['name']
    u=request.GET['uname']
    pwd=request.GET['pwd']
    if len(name)==0 or len(u)==0 or len(pwd)==0:
        msg="Invalid."
    elif name.isspace() or u.isspace() or pwd.isspace():
        msg="Cannot be empty."
    else:
        qs=Users.objects.filter(uname=u)
        if len(qs)==0:
            user=Users(name,u,pwd)
            user.save()
            msg="User registered."
        else:
            msg="Username exists."
    response=render(request,'app1/signup.html',context={'msg':msg})
    return response

def signin_view(request):
    username=request.GET['uname']
    pwd=request.GET['pwd']
    try:
        qs=Users.objects.get(Q(uname=username) & Q(password=pwd))
        response=render(request,'app1/welcome.html',context={'username':username})
    except:
        response=render(request,'app1/signin.html',context={'msg':"Incorrect Username or Password."})
    return response

def change_password_view(request):
    username=request.GET['uname']
    opwd=request.GET['opwd']
    npwd=request.GET['npwd']
    if len(npwd)==0 or npwd==" ":
        msg="Password cannot be empty."
    else:
        try:
            qs=Users.objects.get(Q(uname=username) & Q(password=opwd))
            qs.password=npwd
            qs.save()
            msg="Password changed successfully."
        except:
            msg="Username or old password doesnot match."
    response=render(request,'app1/change_password.html',context={'msg':msg})
    return response