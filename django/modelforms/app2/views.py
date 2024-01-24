from django.shortcuts import render, HttpResponse
from app2.forms import movieform
from app2.models import movie


# Create your views here.

def insert(request):
    var = movieform()
    if request.method=="POST" and request.FILES:
        form=movieform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("data stored in table")
    return render(request, "ins.html", {'var':var})


def update(request, pk):
    data=movie.objects.get(id=pk)
    var = movieform(instance=data)
    if request.method=="POST" and request.FILES:
        form=movieform(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponse("data stored in table")
    return render(request, "ins.html", {'var':var})


def delete(request, pk):
    movie.objects.filter(id=pk).delete()
    return HttpResponse("data deleted from table")