"""core_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import main_app.views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),

    path('api/get_status', main_views.CoursePage.as_view()),                    # GET - gets user status (student or teacher)

    path('api/my_classes', main_views.ShowMyClasses.as_view()),                 # GET - gets classes of current user

    path('api/classes/<int:pk>/', main_views.ShowClass.as_view()),              # GET - gets current block of tasks
    path('api/classes/<int:pk>/new_block', main_views.CreateBlock.as_view()),   # POST - creates new block of tasks
    path('api/blocks/<int:pk>/change', main_views.ChangeBlock.as_view()),       # PUT - changes current block of tasks
    path('api/blocks/<int:pk>/delete', main_views.DeleteBlock.as_view()),       # DELETE - deletes current block of tasks

    path('api/tasks/<int:pk>/', main_views.ShowTask.as_view()),                 # GET - gets current task
    path('api/blocks/<int:pk>/new_task', main_views.CreateTask.as_view()),      # POST - creates new task
    path('api/tasks/<int:pk>/change', main_views.ChangeTask.as_view()),         # PUT - changes current task
    path('api/tasks/<int:pk>/delete', main_views.DeleteTask.as_view()),         # DELETE - deletes current task

    path('api/tasks/<int:pk>/send_code', main_views.CodeChecker.as_view()),     # POST - sends task for checking
]
