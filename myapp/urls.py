from django.urls import path
from . import views


urlpatterns = [
    path("", views.myAppHomeView),
    path("http-page", views.HtmlSamplePage),
]
