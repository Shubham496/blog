from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def myAppHomeView(request):
    return HttpResponse("<h1>my app home</h1>")



def HtmlSamplePage(request):
    return render(request, "sample.html")


def sendingData(request):

    di = {
        'name': "shubham",
        'age': 25,
        'isActive': True,
        "dogs": ["dog1", "dog2"],
        "info": {"edu":"b.tech", "job": "netmax"}

    }
    return render(request, "dataloading.html", context=di)


def base(request):
    return render(request, "base.html")


def extend(request):
    return render(request, 'extend.html')