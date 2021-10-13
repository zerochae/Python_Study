"""HELLO_DJANGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from HELLO_DJANGO import views
# from django.conf.urls.static import static
  
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('hello', views.index, name='hello'),
    # path('param1', views.param1, name='param1'),
    # path('param2', views.param2, name='param2'),
    # path('myforward', views.myforward, name='myforward'),
    path('emp_list', views.emp_list, name='emp_list'),
]