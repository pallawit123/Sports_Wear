from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User




# alliswell123 password

# Index view to check if the user is logged in
# from django.shortcuts import render, redirect
def index(request):
   render(request,'index.html')
   
   
def login(request):
       render(request,'login.html')
       
       
       
def logout(request):
       render(request,'logout.html')
   