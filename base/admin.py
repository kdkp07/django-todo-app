import imp
from django.contrib import admin
# from here
from .models import Task

# Register your models here.

admin.site.register(Task)