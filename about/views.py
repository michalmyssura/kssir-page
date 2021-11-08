from django.shortcuts import render

from .models import About
# Create your views here.

def abouts(request):
    about = About.objects
    return render(request,'about/about.html',{'about':about})
