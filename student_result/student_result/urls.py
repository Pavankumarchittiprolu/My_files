"""
URL configuration for student_result project.

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
    path('add/',add_marks),
    path('update/',update_marks),
    path('find/',find_result),
    path('delete/',delete_stud),
    path("display_results/",view_results),
    path('add_stud/',add_stud_view),
    path('update_view',update_stud_view),
    path('find_result/',find_result_view),
    path("delete_stud_view/",delete_stud_view),
    path('display_results_view/',display_results_view)


]
