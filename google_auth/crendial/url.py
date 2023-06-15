from django.urls import path


from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("home",home,name="home"),
    path('dashboard/', dashboard, name='dashboard'),
    path("logout/", logout,name="logout")
    
    
]