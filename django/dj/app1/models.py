from django.db import models

# Create your models here.

# class emp(models.Model):
#     ename=models.CharField(max_length=20)
#     salary=models.IntegerField()
#     mgr=models.IntegerField()
#     deptno=models.IntegerField()

# CRUD
# CREATE
#     tname.objects.create(colname=value,col2=val2,cal3=val3)
    
# READ
#     VAR = tname.objects.get(col=value) ---> only 1 record returned
#     Var = tname.objects.filter(col=value) ---> returns n values
#     print the filter output with a forloop
#     var = tname.objects.first()
#     var = tname.objects.last()
#     var = tname.objects.all()

# UPDATE 
#     tname.objects.filter(col=value).update()

# DELETE
#   tname.objects.filter(col=value).delete() 
    

# AND
# , is the and operator
# from django.db.models import Q
#     var = tname.objects.filter(Q(col1=val1,col2=val2))

# OR Operator
#     var = tname.objects.filter(col1=val1)|tname.objects.filter(col2=val2)

# NOT operator
#     var = emp.objects.exlude(col1-val1)

# Relational operator 
#     var = tname.objects.filter(colname__gt=value)   greater than operator
#     var = tname.objects.filter(colname__lt=value)   lesser than operator
#     var = tname.objects.filter(colname__gte=value)   greater than equal operator
#     var = tname.objects.filter(colname__lte=value)   lesser than equal operator
#     var = tname.objects.exlude()   

# Multirow functions
#     from django.db.models import Avg, Sum, Min, Max, Count
#     tname.objects.all().aggregate(Avg('colname'))
#     tname.objects.all().aggregate(Sum('colname'))
#     tname.objects.all().aggregate(Min('colname'))
#     tname.objects.all().aggregate(Max('colname'))
#     tname.objects.all().aggregate(Count('colname'))
    
# Order by
    # ascending order
    # var = tname.objects.all().order_by('colname')
    # descending order
    # var = tname.objects.all().order_by('-colname')

# var = tname.objects.filter(colname__startswith=value)
# var = tname.objects.filter(colname__endwith=value)
# var = tname.objects.filter(colname__containswith=value)
    

# model inheritance

class sam(models.Model):
    name = models.CharField(max_length=20)
    mob = models.IntegerField()
    class Meta:
        abstract=True


class student(sam):
    sid = models.IntegerField()


# Proxy model
    
class sample(models.Model):
    name = models.CharField(max_length=10)
    mob = models.IntegerField()
    add = models.CharField(max_length=20)

class s(sample):
    class Meta:
        abstract=True


# class teacher(sam):
#     tsub=models.CharField(max_length=20)




# from app1.models import emp


# 