 
from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name="home"),
    path('collections',views.collections,name="collections"),
    path('login',views.loginn,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('collections/<str:slug>',views.collectionsview,name="collectionsview"),
]
