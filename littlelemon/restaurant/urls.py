from django.contrib import admin
from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemsView

urlpatterns = [
    path('', index, name='index'),
    path('items/', MenuItemsView.as_view()),
    path('items/<int:pk>/', SingleMenuItemsView.as_view()),
]
