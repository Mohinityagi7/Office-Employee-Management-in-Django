from django.contrib import admin
from .models import Employee,Role,Department
# from emp_app.models import Contact

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
