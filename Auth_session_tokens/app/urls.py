from django.contrib import admin
from django.urls import path
from app import views

urlpatterns=[
    path("login/",views.login_view,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout,name="logout"),
    path("dashboard/",views.dashboard,name="dashboard")
]