from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('management/', views.management, name='management'),
    path('management/<str:anything>/', views.management, name='management_catch_all'),
    path('facts/', views.facts, name='facts'),
    path('facts/<str:anything>/', views.facts, name='facts_catch_all'),
    path('news/', views.news, name='news'),
    path('news/<str:anything>/', views.news, name='news_catch_all'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<str:anything>/', views.contacts, name='contacts_catch_all'),
    path('history/', views.history, name='history'),
    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
    path('history/<str:anything>/', views.history, name='history_catch_all'),
]