from email import message
from django.db import models
from django.forms import CharField

# Create your models here.

class Inquiry(models.Model):
    fullname = models.CharField(max_length=64)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)