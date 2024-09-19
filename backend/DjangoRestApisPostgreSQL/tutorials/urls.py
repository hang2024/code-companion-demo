# urls.py in your 'tutorials' app

from django.urls import path
from tutorials import views

urlpatterns = [
    path('tutorials/', views.tutorial_list, name='tutorial_list'),
    path('tutorials/<int:pk>/', views.tutorial_detail, name='tutorial_detail'),
    path('tutorials/published/', views.tutorial_list_published, name='tutorial_list_published'),
]

