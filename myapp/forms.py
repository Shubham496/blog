from django.forms import ModelForm
from .models import Emloyee
# from django.core.exceptions import ValidationError

class EmployeeForm(ModelForm):
    class Meta:
        model = Emloyee
        fields = '__all__'


  