from django.shortcuts import render, HttpResponse
from app1.models import registration
from app1.forms import rgform
from django.contrib.auth.hashers import make_password

# Create your views here.

def registration(request):
    var=rgform(request.POST)
    if request.method=="POST":
        form=rgform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            password=form.password
            form.password=make_password(password)
            form.save()
            return HttpResponse("Registration completed")

    return render(request, "sam.html",{"var":var})


from django.contrib.auth.forms import AuthenticationForm

def logn(request):
    var=AuthenticationForm()
    return render(request, "lgn.html",{"var":var})