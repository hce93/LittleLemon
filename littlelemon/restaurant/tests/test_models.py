from django.test import TestCase
from restaurant import models


class MenuTest(TestCase):
    def test_get_item(self):
        item = models.Menu.objects.create(id = 4, title="Jelly", price=3.50, inventory=35)
        self.assertEqual(str(item), "Jelly : 3.50")