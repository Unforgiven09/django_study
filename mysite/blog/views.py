from .models import Post, Category, Tag
from django.shortcuts import render


def get_categories():
    all = Category.objects.all()
    half = all.count() / 2 + all.count() % 2
    return {'cat1': all[:half], 'cat2': all[half:]}


def index(request):
    posts = Post.objects.all().order_by('-published_date')
    # posts = Post.objects.filter(title__icontains='Новый')
    context = {
        'posts': posts
    }
    context.update(get_categories())
    # context.update(get_tag())
    return render(request, 'blog/index.html', context)


def post(request):
    context = {

    }
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def about(request):
    context = {

    }
    context.update(get_categories())
    return render(request, 'blog/about.html', context)


def services(request):
    context = {
        
    }
    context.update(get_categories())
    return render(request, 'blog/services.html', context)


def contact(request):
    context = {

    }
    context.update(get_categories())
    return render(request, 'blog/contact.html', context)
