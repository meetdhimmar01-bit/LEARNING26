from django.contrib import admin
from .models import Employee
from .models import Employee,Course,Player,teacher
# Register your models here.
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Player)
admin.site.register(teacher)


