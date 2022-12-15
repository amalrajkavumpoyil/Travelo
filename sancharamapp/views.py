from django.http import HttpResponse
from django.shortcuts import render
from . models import place,vlog

# Create your views here.
def fun(request):
    obj=place.objects.all()
    ob=vlog.objects.all()

    return render(request,"index.html",{'results':obj,'new': ob})

# def temp(request):
#     ob=vlog.objects.all()
#     return render(request, "index.html", {'new': ob})


