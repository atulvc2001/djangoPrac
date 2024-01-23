from django.contrib import admin
from app1.models import customer
from app1.models import product

# Register your models here.
admin.site.register(customer)
admin.site.register(product)