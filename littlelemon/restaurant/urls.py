from django.contrib import admin 
from django.urls import path
from . import views 
from rest_framework.authtoken.views import obtain_auth_token

  
urlpatterns = [ 
    path('', views.home, name='home'),
    path('menu/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>', views.SingleMenuItem.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('book/', views.BookingFormView.as_view(), name="book"),
    path('book/success/', views.success, name='success'),
    path('bookings', views.bookings, name='bookings'), 
]

# test - d3221eb00a3375c0b4836ba011b3d9896bbce7b9