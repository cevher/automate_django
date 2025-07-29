from django.contrib import admin

# Register your models here.
from .models import Employee, Student, Customer


admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Employee)
