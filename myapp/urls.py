from django.urls import path
from . import views


urlpatterns = [
    path("", views.myAppHomeView),
    path("http-page/", views.HtmlSamplePage),
    path('sending-data/', views.sendingData),
    path("base/", views.base),
    path("extend/", views.extend)
]
