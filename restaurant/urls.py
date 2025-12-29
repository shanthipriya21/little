from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>/', views.display_menu_item, name='menu_item'),
    path('book/', views.book, name='book'),
    path('get-bookings/', views.get_bookings, name='get_bookings'),
    path('reservations/', views.reservations, name='reservations'),
    path('get-available-slots/', views.get_available_slots, name='get_available_slots'),
]
