from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apartments/', views.ApartmentListView.as_view(), name='apartments'),
    path('apartment/<int:pk>/', views.ApartmentDetailView.as_view(), name='apartment'),
    path('new_reservation/', views.UserReservationCreateView.as_view(), name='user_reservation_create'),
    path('my_reservation/', views.UserReservationListView.as_view(), name='user_reservations'),
    path('update_reservation/<int:pk>/', views.UserReservationUpdateView.as_view(), name='user_reservation_update'),
    path('cancel_reservation/<int:pk>', views.UserReservationDeleteView.as_view(), name='user_reservation_delete'),
]   
