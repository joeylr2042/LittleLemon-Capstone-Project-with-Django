from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MenuItemSerializer

from .models import MenuItem


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemsView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
