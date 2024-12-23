"""
URL configuration for emp_project project.

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
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('add_emp/',add_emp),
    path('delete_emp/',delete_emp),
    path("add_dept/",add_dept),
    
    path('display_dept/',display_dept),
    path('add_dept_view/',add_dept_view),
    path('display_dept_view/',display_dept_view),
    path('add_emp_view/',add_emp_view),
    path('delete_emp_view/',delete_emp_view),
    path('display_emp_view/',display_emp_view),

]
