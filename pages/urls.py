from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='index'),
    path('about/', views.aboutView, name='about'),
    path('contact/', views.contactView, name='contact'),
    path('furniture/', views.furnitureView, name='furniture'),
    path('sale/', views.saleView, name='sale'),
    path('rent/', views.rentView, name='rent'),
    path('sale_details/<str:pk>/', views.saleDetailView, name='sale_details'),
    path('rent_details/<str:pk>/', views.rentDetailView, name='rent_details'),
    path('furn_details/<str:pk>/', views.furnitureDetailView, name='furn_details'),
]
