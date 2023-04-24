from django.urls import path
from  . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('bank', views.bank, name='bank'),
    path('registration',views.registration,name='registration'),
    path('branches',views.branches,name='branches'),
    path('add/',views.addition,name='addition'),
    path('logout', views.logout, name='logout'),




]
