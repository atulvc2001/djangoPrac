from django.db import models

# Create your models here.

class emp(models.Model):
    eno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    emob=models.IntegerField()
    eadd=models.CharField(max_length=20)