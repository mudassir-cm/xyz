from django.shortcuts import render, redirect

from myapp.form import DepartmentForm, EmployeeForm
from myapp.models import Department


def welcome(request):
    return render(request, 'myapp/welcome.html')

def employeeadd(request):
    employee = EmployeeForm
    return render(request, 'myapp/employeeadd.html', {'employee': employee})


def departmentadd(request):
    department = DepartmentForm
    return render(request, 'myapp/departmentadd.html', {'department': department}
    )

def departmentcreate(request):
    dep = DepartmentForm(request.POST)
    dep.save()
    return redirect('/myapp/department/show')

def departmentshow(request):
    list = Department.objects.all()
    return render(request, 'myapp/departmentshow.html', {'list': list})


# Create your views here.
