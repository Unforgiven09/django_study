from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='current_day_index'),
    path('MO/', views.monday, name='current_day_monday'),
    path('TU/', views.tuesday, name='current_day_tuesday'),
    path('WE/', views.wednesday, name='current_day_wednesday'),
    path('TH/', views.thursday, name='current_day_thursday'),
    path('FR/', views.friday, name='current_day_friday'),
    path('SA/', views.saturday, name='current_day_saturday'),
    path('SU/', views.sunday, name='current_day_sunday'),
]