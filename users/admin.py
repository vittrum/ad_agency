from django.contrib import admin

from .models import Client, Employee, EmployeeDepartment, Department

# Register your models here.

admin.site.register(Client)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeDepartment)
