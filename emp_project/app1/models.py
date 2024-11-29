from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=30)

    class Meta:
        db_table="Dept"

    def __str__(self):
        return self.deptno,self.deptname
    
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    job=models.CharField(max_length=30)
    sal=models.FloatField()
    dept=models.ForeignKey(dept,on_delete=models.CASCADE)

    class Meta:
        db_table="Emp"

    def __str__(self):
        return self.empno,self.ename,self.job,self.sal,self.dept




