from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('page/', views.page, name='page'),
    path('page4/', views.page4, name='page4'),
]