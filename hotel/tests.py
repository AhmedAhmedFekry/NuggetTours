from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Hotel

class HotelAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.hotel = Hotel.objects.create(
            name='hotel',
            address='sadat',
            city='sadat',
            country='eygpt',
            price_per_night=Decimal('117.00'),
            is_available=True
        )
        self.hotel1 = Hotel.objects.create(
            name='hotel 1',
            address='badar',
            city='badar',
            country='eygpt',
            price_per_night=Decimal('165.00'),
            is_available=False
        )

    def test_retrieve_all_hotels(self):
        url = reverse('hotel-list')
        response = self.client.get(url, {'page_size': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(len(response.data["results"]), 1)


    def test_create_hotel(self):
        url = reverse('hotel-list')
        data = {
            'name': 'hotel 2',
            'address': 'alex',
            'city': 'alex',
            'country': 'eygpt',
            'price_per_night': '300.00',
            'is_available': True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hotel.objects.count(), 3)


    # Test Price per night cannot be negative when create
    def test_create_hotel_with_negative(self):
        url = reverse('hotel-list')
        data = {
            'name': 'hotel 2',
            'address': 'alex',
            'city': 'alex',
            'country': 'eygpt',
            'price_per_night': '-300.00',
            'is_available': True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['price_per_night'], ["Price per night cannot be negative."])

    def test_update_hotel(self):
        url = reverse('hotel-detail', args=[self.hotel1.id])
        data = {
            'name': 'edit hotel  1',
            'address': 'alex st 100',
            'city': 'alex',
            'country': 'eygpt',
            'price_per_night': '300.00',
            'is_available': False
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'edit hotel  1')
        self.assertEqual(response.data['address'], 'alex st 100')
        self.assertEqual(response.data['city'], 'alex')
        self.assertEqual(response.data['price_per_night'], '300.00')
        self.assertEqual(response.data['is_available'], False)


   # Test Price per night cannot be negative when update 
    def test_update_hotel_with_negative(self):
        url = reverse('hotel-detail', args=[self.hotel1.id])
        data = {
            'name': 'edit hotel  1',
            'address': 'alex st 100',
            'city': 'alex',
            'country': 'eygpt',
            'price_per_night': '-300.00',
            'is_available': False
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['price_per_night'], ["Price per night cannot be negative."])

    def test_delete_hotel(self):
        url = reverse('hotel-detail', args=[self.hotel1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Hotel.objects.count(), 1)

    def test_hotels_filter_by_price_range(self):
        url = reverse('hotel-list')
        response = self.client.get(url, { 'page_size': 1,'min_price': '150.00', 'max_price': '300.00'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]['city'], 'badar')
        self.assertEqual(response.data["results"][0]['name'], 'hotel 1')

    def test_hotels_filter_by_city(self):
        url = reverse('hotel-list')
        response = self.client.get(url, {'page_size': 1,'city': 'badar'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]['name'], 'hotel 1')

    def test_hotels_filter_by_country(self):
        url = reverse('hotel-list')
        response = self.client.get(url, {'page_size': 1,'country': 'eygpt'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)


    def test_hotels_filter_by_available(self):
        url = reverse('hotel-list')
        response = self.client.get(url, {'page_size': 1,'available': 'true'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

