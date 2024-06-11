from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create some test instances of the Menu model
        Menu.objects.create(Title="Pizza", price=10, inventories=50)
        Menu.objects.create(Title="Burger", price=8, inventories=30)

    def test_getall(self):
        # Get all Menu objects
        client = APIClient()
        url = reverse('menu')  # Assuming 'menu-list' is the URL name for listing menus
        response = client.get(url)
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Retrieve data from the response
        data = response.data
        
        # Serialize the Menu objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Check if the serialized data matches the response data
        self.assertEqual(data, serializer.data)
