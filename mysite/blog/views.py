import random
from django.shortcuts import render


def show_num():
    return random.randint(1, 10)


def index(request):
    context = {

    }
    return render(request, 'blog/index.html', context)


def post(request):
    context = {

    }
    return render(request, 'blog/post.html', context)


def about(request):
    context = {

    }
    return render(request, 'blog/about.html', context)


def services(request):
    context = {
        
    }
    return render(request, 'blog/services.html', context)


def contact(request):
    context = {

    }
    return render(request, 'blog/contact.html', context)
