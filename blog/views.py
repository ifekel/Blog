from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    
    context = {'posts': posts}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def post(request, pos):
    post = Post.objects.get(id=pos)
    
    context = {'post': post}
    return render(request, 'post.html', context)