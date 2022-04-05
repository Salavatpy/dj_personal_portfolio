from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(requst, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(requst, 'blog/detail.html', {'blog':blog})
