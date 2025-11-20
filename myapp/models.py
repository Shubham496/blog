from django.db import models

# Create your models here.
class student(models.Model):
    roll_No = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.roll_No} {self.name}'
    

class customers(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(blank=True, max_length=25)



class Emloyee(models.Model):
    name = models.CharField(max_length=20)
    salary = models.IntegerField(null=True, blank=True)
    age = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    email = models.EmailField( max_length=254, blank=True, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50)


from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField( User ,on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)