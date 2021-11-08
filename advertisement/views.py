from django.shortcuts import render
from .models import Advertisement


def home(request):
    advertisements=Advertisement.objects
    return render(request, 'advertisement/index.html', {'advertisements':advertisements})

