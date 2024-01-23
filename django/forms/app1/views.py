from django.shortcuts import render,HttpResponse
# from app1.models import sample
from app1.models import customer
from .forms import customerform

# Create your views here.
def insert(request):
        form = customerform()
        if request.method=='POST':
                form = customerform(request.POST)
                if form.is_valid():
                        name = form.cleaned_data['cname']
                        mob = form.cleaned_data['mob']
                        addr = form.cleaned_data['addrs']
                        customer.objects.create(cname=name,mob=mob,addrs=addr)
                        return HttpResponse('data stored in the table')
        return render(request, "sam.html", {'form':form})
    
def read(request):
        var = customer.objects.all()
        return render(request, "read.html", {'var':var})

def update(request, pk): 
        form = customerform()
        if request.method=='POST':
                form = customerform(request.POST)
                if form.is_valid():
                        name = form.cleaned_data['cname']
                        mob = form.cleaned_data['mob']
                        addr = form.cleaned_data['addrs']
                        customer.objects.filter(id=pk).update(cname=name,mob=mob,addrs=addr)
                        return HttpResponse('data Updated in the table')
        return render(request, "sam.html", {'form':form})

def delete(request, pk):
        customer.objects.filter(id=pk).delete()
        return HttpResponse("Data deleted from table")


# ? This was the previous form without using django forms
# def insert(request):
#     if request.method == "POST":
#         name = request.POST["name"]
#         age = request.POST["age"]
#         dob = request.POST["dob"]
#         email = request.POST["email"]
#         sample.objects.create(name=name,age=age,dob=dob,email=email)
#         return HttpResponse("data stored in the table")

#     return render(request, "sam.html")

# def read(request):

#     var = sample.objects.all()

#     return render(request,"read.html",{'var':var})

# def update(request,pk):
#     if request.method == "POST":
#         name = request.POST["name"]
#         age = request.POST["age"]
#         dob = request.POST["dob"]
#         email = request.POST["email"]
#         sample.objects.filter(id=pk).update(name=name,age=age,dob=dob,email=email)
#         return HttpResponse('Data updated in table')
#     return render(request,"sam.html")


# def delete(request,pk):
#     sample.objects.filter(id=pk).delete()
#     return HttpResponse('Data deleted from a table')