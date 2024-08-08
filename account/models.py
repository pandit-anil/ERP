from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    DEPARTMENT_CHOICE = [
        ('HR', 'Human Resource'),
        ('SALES','sales'),
        ('IT', 'IT Department'),
    ]

    ROLE_CHOICE =[
        ('ADMIN','Administrator'),
        ('MANAGER', 'Manager'),
        ('EMPLOYEE', 'Employee')
    ]
    
    department = models.CharField(max_length=70, choices=DEPARTMENT_CHOICE)
    role = models.CharField(max_length=70, choices= ROLE_CHOICE)
    mobile = models.CharField(max_length=10)
    profile = models.ImageField(upload_to='profile')
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name
    