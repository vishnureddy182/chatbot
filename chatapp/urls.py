from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_endpoint, name='chat_endpoint'),
    path('clear/', views.clear_chat, name='clear_chat'),
]