from django.contrib import admin

# Register your models here.
from super_admin.models import Employee, LeaveManagement, TaskManagement

admin.site.register(Employee)
admin.site.register(LeaveManagement)
admin.site.register(TaskManagement)