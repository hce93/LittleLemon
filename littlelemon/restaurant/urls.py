from django.contrib import admin 
from django.urls import path
from . import views 
from rest_framework.authtoken.views import obtain_auth_token

  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItem.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]

# test - d3221eb00a3375c0b4836ba011b3d9896bbce7b9