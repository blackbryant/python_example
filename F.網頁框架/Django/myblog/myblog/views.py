from django.shortcuts import render,redirect
from django.http import HttpResponse
from myblog.models import Post
from myblog.models import Product
from datetime import datetime

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now
    return render(request,"index.html",locals())

def showpost(request,slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None :
            return render(request,"post.html",locals())
    except:
        redirect('/')
    
def about(request):
    try:
        products = Product.objects.all()
        if products !=None:
            return render(request,"about.html",locals())
    except:
        redirect("/")
