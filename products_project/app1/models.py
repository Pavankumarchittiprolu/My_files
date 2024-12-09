from django.db import models

# Create your models here.
class Products(models.Model):
    prodId=models.CharField(max_length=20,primary_key=True)
    prodname=models.CharField(max_length=20)
    qty=models.IntegerField()
    price=models.FloatField()

    class Meta:
        db_table="Products"

