# from django.urls import re_path

# from tutorials import views 
 
# urlpatterns = [ 
#     re_path(r'^api/tutorials$', views.tutorial_list),
#     re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
#     re_path(r'^api/tutorials/published$', views.tutorial_list_published)
# ]
# urls.py

from django.urls import path
from tutorials import views

urlpatterns = [
    path('api/tutorials', views.tutorial_list, name='tutorial_list'),
    path('api/tutorials/<int:pk>', views.tutorial_detail, name='tutorial_detail'),
    path('api/tutorials/published', views.tutorial_list_published, name='tutorial_list_published'),
]
