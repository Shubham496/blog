from django.urls import path
from . import views


urlpatterns = [
    path("", views.myAppHomeView, name="home"),
    path("http-page/", views.HtmlSamplePage),
    path('sending-data/', views.sendingData),
    path("base/", views.base),
    path("extend/", views.extend, name="Extend"),
    path("employees/<int:id>", views.employee_detail_view, name="employee"),
    path("employees/salary/<int:salary>", views.filterEmployee),
    
    path("employees/", views.all_employee_view, name="all_employees"),
    path("activeEmp/", views.ActiveEmployees),
    path("employee/create/", views.createNewEmployee),
    path("employee/Delete/<int:id>/", views.DeleteEmployeeView, name='empDelete'),
    path("profile/", views.profile),
]
