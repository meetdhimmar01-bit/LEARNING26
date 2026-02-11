from django import forms
from .models import Employee,Course,Player,teacher

#employee form
#modelForm -->it will create form using model fileds
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'        

class teacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = '__all__'                  