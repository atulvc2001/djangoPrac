from django.shortcuts import render, HttpResponse
from app2.forms import movieform


# Create your views here.

def insert(request):
    var = movieform()
    if request.method=="POST" and request.FILES:
        form=movieform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("data stored in table")
    return render(request, "ins.html", {'var':var})