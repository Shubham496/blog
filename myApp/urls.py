from django.urls import path
from .views import *

urlpatterns = [
    path("", product),
    path("1/", product1),
    path("2/", product1)
]
