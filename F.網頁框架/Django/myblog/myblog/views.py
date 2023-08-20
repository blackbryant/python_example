from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Post


def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts)




