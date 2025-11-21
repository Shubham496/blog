from django.shortcuts import render, redirect

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





from .models import *
from .forms import EmployeeForm

def all_employee_view(request):
    emp = Emloyee.objects.all()
    data = {"data": emp}
    return render(request, "all_employee.html", context=data)




def employee_detail_view(request, id):
    emp = Emloyee.objects.get(id=id)
    empForm = EmployeeForm(instance=emp)

    if request.method == "POST":
        empForm = EmployeeForm(request.POST, instance=emp)
        if empForm.is_valid():
            empForm.save()

    data = {'formData':empForm, "employee": emp}
    return render(request, "employee.html", data)



from django.shortcuts import render, redirect

def createNewEmployee(request):
    empForm = EmployeeForm()
    if request.method == "POST":
        empForm = EmployeeForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return redirect("all_employees")
    data = {'formData':empForm}
    return render(request, "employee.html", data)




def DeleteEmployeeView(request, id):
    emp = Emloyee.objects.get(id = id)
    emp.delete()
    return redirect("all_employees")



def ActiveEmployees(request):
    emp = Emloyee.objects.filter(isActive = True)
    data = {"data": emp}
    return render(request, "all_employee.html", context=data)


def filterEmployee(request, salary):
    emp = Emloyee.objects.filter(salary__gte = salary)
    data = {"data": emp}
    return render(request, "all_employee.html", context=data)






















from django.contrib.auth.models import User


from django.contrib.auth import logout, login, authenticate


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if not user:
            data = {"message":"incorrect username or password"}
            return render(request, 'signin.html', data)
        login(request, user=user)
        return redirect("profile")
    return render(request, 'signin.html')







def profile(request, id=1):
    profile = request.user
    if not request.user.is_authenticated:
        return redirect('home' )
    user = UserProfile.objects.get(user=profile)
    data = {"data": user}
    return render(request,"profile.html", data)
        





