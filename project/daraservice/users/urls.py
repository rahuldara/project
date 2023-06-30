from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('profile/',views.profile,name='user-profile'),
    path('signup/',views.sign_up,name='user-sign-up'),
    path('',auth_view.LoginView.as_view(template_name='users/login.html'),name='users-login'),
        path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='users-logout'),
    
]
