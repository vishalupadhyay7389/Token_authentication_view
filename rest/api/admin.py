from django.contrib import admin
from .models import School , Student , Email


# Register your models here.
admin.site.register([Student, School , Email])
