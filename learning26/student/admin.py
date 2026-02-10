from django.contrib import admin
from .models import Student,Product 
from .models import Student,Product,StudentProfile,Category,Service

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)