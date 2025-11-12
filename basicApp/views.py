from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    name = "shubham"
    age = 25
    dogs = ['dog1', 'dog2']
    info = {"b.tech": 'RJIT', "job": "netmax"}
    isActive = False
    di = {'name': name, "age": age, 'dogs': dogs, 'info': info, 'active': isActive}
    return render(request, "base.html", context= di)



def about(request):
    return render(request, 'about.html')