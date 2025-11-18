from django.contrib import admin

# Register your models here.
from .models import student, customers, Emloyee

admin.site.register(student)


admin.site.register(customers)
admin.site.register(Emloyee)