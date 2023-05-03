from django.contrib import admin    
from django.urls import path
from home import views
from .views import HomePage, Register, Login, test, logoutuser
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.cont,name='contact'),
    path("admine",views.admine,name="admine"),
    path("profile",views.profile,name="profile"),
    path('register/',views.Register, name="register-page"),
    path('login/', views.Login, name="login-page"),
    path('logout/', views.logoutuser, name='logout'),
    path('home-page',views.login,name='home-page')
]
 