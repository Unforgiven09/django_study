from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('post/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]