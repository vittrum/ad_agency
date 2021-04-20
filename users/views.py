from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Client, EmployeeDepartment, Department, Employee


def index(request):
    """
    Displaying homepage for users
    """
    employees = Employee.objects.all()
    departments = Department.objects.all()
    clients = Client.objects.all()

    return render(request, 'index.html',
                  context={'clients': clients, 'employees': employees, 'departments': departments})


class ClientListView(generic.ListView):
    model = Client


class ClientDetailView(generic.DetailView):
    model = Client


class DepartmentListView(generic.ListView):
    model = Department
