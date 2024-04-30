from django.contrib import admin
from .models import student
# Register your models here.

models_list= [student]
admin.site.register(models_list)