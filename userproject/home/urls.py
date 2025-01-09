from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index, name=''),  # Index page
    path('login/', views.login, name='login'),  # Login page
    path('logout/', views.logout, name='logout'),  # Logout functionality
    # path('home/', views.home, name='home'),  # Home page for logged-in users
]
