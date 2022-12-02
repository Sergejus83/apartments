from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apartments/', views.ApartmentListView.as_view(), name='apartments'),
    path('apartment/<int:pk>/', views.ApartmentDetailView.as_view(), name='apartment')

]
