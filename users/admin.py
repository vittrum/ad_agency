from django.contrib import admin

from .models import Client, Employee, EmployeeDepartment, Department

# Register your models here.

# TODO: rebuild admin panel in list view
# TODO: add filtering to admin panel
# TODO: enhance connections in admin panel

admin.site.register(Client)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeDepartment)
