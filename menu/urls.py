from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('order/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),
    path('staff/orders/', views.staff_dashboard, name='staff_dashboard'),
    path('staff/orders/', views.staff_order_dashboard, name='staff_order_dashboard'),

]