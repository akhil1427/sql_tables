from django.db import models

# Create your models here.

class EmployeeTable(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=50)
    Job=models.CharField(max_length=20)
    Mgr=models.IntegerField()
    Hire_Date=models.DateField()
    Sal=models.IntegerField()
    Comm=models.IntegerField(null=True,blank=True)
    Dept_No=models.IntegerField()
    def __str__(self):
        return self.Ename
class DEPT(models.Model):
    Dept_no=models.OneToOneField(EmployeeTable,on_delete=models.CASCADE)
    D_Name=models.CharField(max_length=20)
    Loc=models.CharField(max_length=30)
    def __str__(self):
        return  str (self.pk)

class SalGrade(models.Model):
    Grade=models.IntegerField()
    Losal=models.IntegerField()
    Hisal=models.IntegerField()
    Loc=models.OneToOneField(DEPT,on_delete=models.CASCADE)

    

    
