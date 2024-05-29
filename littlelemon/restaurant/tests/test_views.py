from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a token for the user
        self.token = Token.objects.create(user=self.user)

        # Set the token in the header
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create test instances of the Menu model
        self.menu1 = MenuItem.objects.create(title='Breakfast', price=5.99)
        self.menu2 = MenuItem.objects.create(title='Lunch',  price=9.99)
        self.menu3 = MenuItem.objects.create(title='Dinner', price=14.99)

    def test_getall(self):
        # Get response from the view
        response = self.client.get(reverse('menu_items'))  # 'menu-list' refers to the name in urls.py

        # Get all Menu objects from the database
        menus = MenuItem.objects.all()

        # Serialize the data
        serializer = MenuItemSerializer(menus, many=True)

        # Assert that the response data matches the serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)