from django.contrib import admin
from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('items/', MenuItemsView.as_view()),
    path('items/<int:pk>/', SingleMenuItemsView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]

