from django.urls import path
from .import views
from django.contrib import admin
from django.shortcuts import render,redirect,get_object_or_404
from .models import PostModel
from .forms import PostModelForm

urlpatterns = [
        
    
  
    path('blog',views.index,name='blog-index'),
 
]



