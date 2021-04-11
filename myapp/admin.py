from django.contrib import admin

from .models import Department, Employee

class EmployeeTabularInline(admin.TabularInline):
    model = Employee

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [EmployeeTabularInline]
    class Meta:
        model = Department


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee)

# Register your models here.
