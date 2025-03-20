from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('de/', views.de, name='deutsch'),
    path('fr/', views.fr, name='french'),
]