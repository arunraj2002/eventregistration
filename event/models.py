from django.db import models

# Create your models here.

from django.contrib import admin
class participant(models.Model):
    username=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    institution=models.CharField(max_length=100)

class participantAdmin(admin.ModelAdmin):
    list_display=("username", "phone", "email", "institution")
