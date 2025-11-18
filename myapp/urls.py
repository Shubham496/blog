from django.urls import path
from . import views


urlpatterns = [
    path("", views.myAppHomeView, name="home"),
    path("http-page/", views.HtmlSamplePage),
    path('sending-data/', views.sendingData),
    path("base/", views.base),
    path("extend/", views.extend, name="Extend"),
    path("employees/", views.all_employee_view, name="all_employees"),
    path("employees/<int:id>", views.employee_detail_view, name="employee")
]
