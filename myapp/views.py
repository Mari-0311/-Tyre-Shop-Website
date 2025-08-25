from django.shortcuts import render

# Create your views here.
def mo(request):
    return render(request,"mo.html")


def about(request):
    return render(request,"about.html")

def review(request):
    return render(request,"review.html")

def service(request):
    return render(request,"service.html")

def wheels(request):
    return render(request,"wheels.html")





