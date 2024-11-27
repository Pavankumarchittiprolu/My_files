from django.db import models

# Create your models here.
class students(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    subject1=models.FloatField()
    subject2=models.FloatField()

    
