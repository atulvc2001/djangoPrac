from django.db import models

# Create your models here.


class customer(models.Model):
    cname = models.CharField(max_length=20)
    mob = models.IntegerField()
    addrs = models.CharField(max_length=40)
    def __str__(self):
        return self.cname   

class product(models.Model):
    pname=models.CharField(max_length=20)
    price=models.IntegerField()
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.pname 
    
class sample(models.Model):
    sno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)