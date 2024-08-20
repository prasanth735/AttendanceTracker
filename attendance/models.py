from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Employee(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    employee_id=models.CharField(max_length=50)
    department=models.CharField(max_length=200)
    job_title=models.CharField(max_length=200)


    def __str__(self):
        return self.user.username


class Attendance(models.Model):

    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    date=models.DateField()
    ATTENDANCE_STATUS=(
        ('A','present'),
        ('A','absent'),
        ('L','late'),
        ('H','halfday')
    )

    attendance_status=models.CharField(max_length=1,choices=ATTENDANCE_STATUS)


    def __str__(self):
        return f"{self.employee.user.username} - {self.date} - {self.attendance_status}"