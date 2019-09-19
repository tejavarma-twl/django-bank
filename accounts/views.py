from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Accounts

# Create your views here.
def home(request):
    data = {
        'email':'nothing',
        'password':'nothing'
    }
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            print('user valid!')
    return render(request,'index.html',data)

def register(request):
    if request.POST:
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
    return render(request,'register.html',{})

def about(request):
    # return HttpResponse("About Django!")
    return render(request,'about.html',{})

def contact(request):
    # return HttpResponse("Contact Django!")
    return render(request,'contact.html',{})

def profile(request):
    # acc = Accounts.objects.create(first_name='Tej',last_name='v',balance=200)
    # acc.save()
    users = Accounts.objects.all()
    for u in users:
        print(u.first_name)

    data = {
        'username':'Varma',
        'email':'varma@gmail.com',
        'address':'Visakhapatnam',
        'designation':'Developer',
        'myusers':users
    }
    return render(request,'profile.html',data)