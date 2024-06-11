from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", price=80.00, inventories=100)
        
        # Assert that the created item has the correct attributes
        self.assertEqual(item.Title, "IceCream")
        self.assertEqual(item.price, 80.00)
        self.assertEqual(item.inventories, 100)

