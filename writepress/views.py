from django.shortcuts import render
from managepost.models import Post
from django.http import HttpResponse


def home(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'post': post})

def details(request, id):
    try:
        post = Post.objects.get(id=id)
        return render(request, 'details.html', {'post': post})
    except Post.DoesNotExist:
        return HttpResponse("Post not found", status=404)