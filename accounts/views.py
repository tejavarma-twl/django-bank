from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    data = { 'name':'Python', 'page':'Home' }
    # return HttpResponse("<h1>Hello Django!</h1>")
    return render(request,'index.html',data)

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