from django.shortcuts import render
import datetime

today = datetime.date.today()
day_num = today.weekday()


class DaysOfWeek:
    def __init__(self, num, link):
        self.num = num
        self.link = link


def index(request):
    context = {'all_days': all_days, 'today': day_num}

    return render(request, 'days/index.html', context)


def monday(request):
    context = {}
    return render(request, 'days/monday.html', context)


def tuesday(request):
    context = {}
    return render(request, 'days/tuesday.html', context)


def wednesday(request):
    context = {}
    return render(request, 'days/wednesday.html', context)


def thursday(request):
    context = {}
    return render(request, 'days/thursday.html', context)


def friday(request):
    context = {}
    return render(request, 'days/friday.html', context)


def saturday(request):
    context = {}
    return render(request, 'days/saturday.html', context)


def sunday(request):
    context = {}
    return render(request, 'days/sunday.html', context)



mo = DaysOfWeek(0, f'MO')
tu = DaysOfWeek(1, f'TU')
we = DaysOfWeek(2, f'WE')
th = DaysOfWeek(3, f'TH')
fr = DaysOfWeek(4, f'FR')
sa = DaysOfWeek(5, f'SA')
su = DaysOfWeek(6, f'SU')

all_days = [mo, tu, we, th, fr, sa, su]
