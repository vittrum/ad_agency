from django.db import models

# Create your models here.
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('clients', args=[str(self.id)])

    class Meta:
        db_table = 'clients'


class Employee(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        db_table = 'employees'


class Department(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'departments'


class EmployeeDepartment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, default='employee')

    def __str__(self):
        return f'{self.employee.last_name} from {self.department.name}'

    class Meta:
        db_table = 'employees_departments'
