from django.db import models
from account.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True , related_name='departments')
    
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(unique=True)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        
    def __str__(self):
        return self.user.name
    
class Attendance(models.Model):
    ATTENDANCE_STATUS_CHOICES =[
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LEAVE', 'On Leave'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=60, choices=ATTENDANCE_STATUS_CHOICES)
    
    def __str__(self):
        return f'{self.employee.user.name} - {self.date}'
    

class LeaveRequest(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('CASUAL', 'Casual Leave'),
        ('SICK', 'Sick Leave'),
    ]
    
    LEAVE_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ] 
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=50, choices=LEAVE_STATUS_CHOICES)
    
    def __str__(self):
        return f'{self.employee.user.name} - {self.leave_type}'
    
    
    
