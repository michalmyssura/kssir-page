from django.urls import path

from . import views

urlpatterns =[
    path('',views.abouts, name='abouts')
]