from django.shortcuts import render

from .models import Post

def post (request):
    posts= Post.objects
    return render(request,'post/post.html',{'posts':posts})