"""
URL configuration for ecommerce project.

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
from shop import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'shop'
urlpatterns = [
   path('',views.allcategories,name="categories"),
   path('products/<int:id>/',views.allproducts,name="products"),
   path('details/<int:id>/',views.details,name="details"),
   path('register/', views.register, name="register"),
   path('login/', views.login, name="login"),
   path('logout/', views.logout, name="logout"),
   path('addcategory/', views.add_category, name="add_category"),
   path('addproduct/', views.add_product, name="add_product"),
   path('addstock/<int:p>/', views.add_stock, name="add_stock"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)