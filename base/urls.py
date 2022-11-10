from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.user_login_page, name="login"),
    path('',views.home, name="home"),
    path('room/<str:pk>/',views.room, name="room")
]