from django import forms  
from emp.models import Emp 
    
class EmployeeForm(forms.ModelForm):  
    
    class Meta:  
        model = Emp
        fields = "__all__"  