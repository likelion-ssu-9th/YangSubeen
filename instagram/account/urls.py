from django.urls import path
from insta import views as first

urlpatterns = [
    path('login/', first.login, name = "login"),
    path('logout/', first.logout, name="logout" ),
    path('signup/',first.register, name = "signup"),

]