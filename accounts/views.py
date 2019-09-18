from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
    data = {
        'username':'Varma',
        'email':'varma@gmail.com',
        'address':'Visakhapatnam',
        'designation':'Developer'
    }
    return render(request,'profile.html',data)