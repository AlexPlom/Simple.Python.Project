from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def index(request):
    posts = Posts.objects.all()[:10]
    
    context  = {
        'posts' : posts
    }

    return render(request,'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html',context)
    

def delete(request, id):
    post = Posts.objects.get(id=id)

    Posts.objects.filter(id=id).delete()
    context = {
        'post': post
    }

    return render(request,'posts/deleteSuccessfull.html', context)