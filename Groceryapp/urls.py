from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('manage_credit/', views.manage_credit, name='manage_credit'),
]