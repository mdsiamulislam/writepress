from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse

def create_post_home(request):
    return render(request, 'managepost/create.html')

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        new_post = models.Post(title=title, description=description, author=author, image=image)
        new_post.save()
        return redirect('home')
    return render(request, 'managepost/create.html')