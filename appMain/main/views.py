from django.shortcuts import render
from main.models import Post
# Create your views here.


def index(request):
    post = Post.objects.all()

    context = {
        "title": "Главная страница",
        "post": post
    }

    return render(request, 'main/index.html', context=context)