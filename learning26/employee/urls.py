from . import views
from django.urls import path

app_name = 'employee'
urlpatterns = [
     path('', views.employeeList, name='employeeList'),
     path('add/',views.addEmployee,name='addEmployee'),
    
    path('employeeFilter/', views.employeeFilter),
    path('createemployee/',views.createEmployee),
    path('createEmployeewithForm/',views.createEmployeewithForm,name='createEmployeeWithForm'),
    path('createCourse/',views.createCourse),
    #path('deleteEmployee/',views.deleteEmployee,name="deleteEmployee"),
    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
    path('update/<int:id>/', views.updateEmployee, name='updateEmployee'),
    path('delete/<int:id>/', views.deleteEmployee, name='deleteEmployee'),
    
]