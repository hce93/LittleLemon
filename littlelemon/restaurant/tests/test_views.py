from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json
from restaurant import models
from restaurant import serializers


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', password='password123')
        # create menu_item object and store as attribute in self
        self.menu_item = models.Menu.objects.create(title='Burger', price=9.99, inventory=50)
        self.url = reverse('menu') 
        
    def test_get_all(self):
        # below is needed if we set permission classes for the user
        # self.client.force_authenticate(user = self.user)
        
        # send a GET request to the URL endpoint
        response = self.client.get(self.url)
        # test status code of reuqets
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        serialized_menu_item = serializers.MenuSerializer(instance = self.menu_item).data
        # response_data = json.loads(response.content.decode('utf-8'))
        print(serialized_menu_item)
        # print(response.data)
        # test GET request
        self.assertContains(response, "Burger")
        
        
    def test_create_menu_item(self):
        new_menu_item_data = {'id':1, 'title': 'Rissotto', 'price': '12.99', 'inventory': 30}

        # Make a request to create a new menu item
        response = self.client.post(self.url, new_menu_item_data, format='json')

        # Assert the expected behavior based on the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the new menu item was created in the database
        self.assertTrue(models.Menu.objects.filter(title='Rissotto').exists())