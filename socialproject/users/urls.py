from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from re import template

urlpatterns = [
   path('',views.index, name='index'),
   path('login/',views.user_login,name='login'),
   path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
   path('password_change/',auth_view.PasswordChangeView.as_view(),name='password_change'),
]