from django.urls import path
from . import views
urlpatterns = [
    path('chat_with_kimihelp/', views.chat_with_kimihelp,name='chat_with_kimihelp'),
]