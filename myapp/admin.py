from django.contrib import admin

# Register your models here.
from .models import student, customers, Emloyee, UserProfile

admin.site.register(student)


admin.site.register(customers)
admin.site.register(Emloyee)
admin.site.register(UserProfile)