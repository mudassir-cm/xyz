from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.welcome),
    path('employee/add/', views.employeeadd),
    path('department/add', views.departmentadd),
    path('department/show', views.departmentshow),
    path('department/create/', views.departmentcreate),
   # path('employee/add', views.employeeadd),
    #path('employee/show', views.employeeshow),
    #path('employee/create/', views.employeecreate),
]