from django.contrib import admin 
from django.urls import path
from . import views 
from rest_framework.authtoken.views import obtain_auth_token

  
urlpatterns = [ 
    path('', views.home, name='home'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItem.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('book/', views.BookingFormView.as_view(), name="book"),
    path('book/success/', views.success, name='success'),
    path('bookings', views.bookings, name='bookings'), 
    path('about/', views.about, name="about"),
    path('managers/', views.AddManager.as_view(), name='manager')
]


# newUser
# oranges123
# 29229715acebcc005fc3a4b10e6c3274d119e9f7