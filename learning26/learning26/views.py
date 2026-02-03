from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse





def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")





