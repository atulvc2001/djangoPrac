from django.shortcuts import render, HttpResponse


# Create your views here.
def fun(request):
    return HttpResponse("Hello")


def sam(request):
    return render(request, "sample.html")


def flp(request, var1, var2, num):
    print(var1)
    return render(
        request,
        "flp.html",
        {
            "m1": var1,
            "m2": var2,
            "message": "Hello, this is from the flp views",
            "message2": "This is the second message",
            "num": num,
        },
    )


def func(request):
    A = [1, 2, 3, 4, 5, 6]
    print(A)
    return render(request, "flp.html", {"B": A})


def page1(request):
    return render(request, "page1.html")


def page2(request):
    return render(request, "page2.html")


def page3(request):
    return render(request, "page3.html")
