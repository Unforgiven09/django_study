from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, 'blog2/index.html', context)


def archives(request):
    context = {

    }
    return render(request, 'blog2/archives.html', context)


def blog(request):
    context = {

    }
    return render(request, 'blog2/blog.html', context)


def demo(request):
    context = {

    }
    return render(request, 'blog2/demo.html', context)


def page(request):
    context = {

    }
    return render(request, 'blog2/page.html', context)


def single(request):
    context = {

    }
    return render(request, 'blog2/single.html', context)


def about(request):
    context = {

    }
    return render(request, 'blog2/about.html', context)
