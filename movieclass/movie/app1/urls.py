"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views

app_name="app1"

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.home.as_view(),name="home"),
    # path('add/',views.add,name="add"),
    path('add/',views.add.as_view(),name='add'),
    # path('detail/<int:i>',views.detail,name="detail"),
    path('edit/<int:pk>',views.edit.as_view(),name="edit"),
    path('detail/<int:pk>',views.detail.as_view(),name="detail"),
    path('delete/<int:pk>',views.delete.as_view(),name="delete"),
    # path('delete/<int:i>',views.delete,name="delete"),
    # path('edit/<int:i>',views.edit,name="edit"),

]
