from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def product(request):
    return  HttpResponse("this is product page")

def product1(request):
    return  HttpResponse("this is product 1 page ")

def product2(request):
    return  HttpResponse("this is product 2 page") 