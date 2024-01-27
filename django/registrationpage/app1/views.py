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
from django.contrib.auth import authenticate,login,logout

def logn(request):
    var=AuthenticationForm()
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        var=authenticate(username=username,password=password)
        if var is not None:
            login(request, var)
            return HttpResponse('login successfully')

    return render(request, "lgn.html",{"var":var})

def logt(request):
    logout(request)
    return HttpResponse("Successfully Logged out")