from django.shortcuts import render, HttpResponse
from aoo1.forms import empform
from aoo1.models import emp



# Create your views here.

def insert(request):
    var=empform()
    if request.method=="POST":
        form=empform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data stored in a table')
    return render(request, "ins.html",{"var":var})

def read(request):
    var = emp.objects.all()
    return render(request, "read.html",{'var':var})

def delete(request,pk):
    emp.objects.filter(eno=pk).delete()
    return HttpResponse("Data deleted from the table")

def update(request,pk):
    data=emp.objects.get(eno=pk)
    var=empform()
    if request.method=="POST":
        form=empform(request.POST, instance=data)
        if form.is_valid():
            form.save() 
            return HttpResponse('data stored in a table')
    return render(request, "ins.html",{"var":var})