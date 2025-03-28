from django.shortcuts import render
from .models import Teachers, Students, Courses


def index(request):
    context = {
        'teachers': Teachers.objects.all(),
        'students': Students.objects.all(),
        'courses': Courses.objects.all(),
    }
    return render(request, 'itstep/index.html', context)
