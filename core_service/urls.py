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
# djoser.url.jwt
import main_app.views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),

    # auth/jwt/create
    # auth/jwt/refresh
    # auth/jwt/verify
    path('api/my_classes', main_views.ShowMyClasses.as_view()),
    path('api/classes/<int:pk>/', main_views.ShowClass.as_view()),
    path('api/classes/<int:pk>/new_sprint', main_views.CreateSprint.as_view()),
    path('api/tasks/<int:pk>/', main_views.ShowTask.as_view()),
    # path('show_info/', main_views.CheckUser.as_view()),
]
