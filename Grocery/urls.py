"""
URL configuration for Grocery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
#we are accessing the views file of this very app(adminapp)
from Groceryapp import views
#from .views import issue_item
#we are accessing the functionality to login#
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),  # For admin panel
    path('',views.index,name = 'index'),
    path('home/',views.home,name = 'home'),
    path('manage_credit/', views.manage_credit, name='manage_credit'),  # For adding a new credit sale
    path('edit_credit_sale/<int:credit_sale_id>/', views.manage_credit, name='edit_credit_sale'),  # For editing an existing credit sale
    path('delete_credit_sale/<int:credit_sale_id>/', views.delete_credit_sale, name='delete_credit_sale'),
    path('logout/',auth_views.LoginView.as_view(template_name = 'Groceryapp/logout.html'),name='logout'),
    path('home/<int:product_id>/',views.product_detail,name = 'product_detail'),
    path('delete/<int:product_id>/',views.delete_detail,name = 'delete_detail'),
    path('issue_item/<int:pk>/', views.issue_item, name='issue_item'),
    path('receipt/',views.receipt,name='receipt'),
    path('receipt/<int:receipt_id>/',views.receipt_detail, name='receipt_detail'),
    path('login/',auth_views.LoginView.as_view(template_name = 'Groceryapp/login.html'),name = 'login'),
]