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