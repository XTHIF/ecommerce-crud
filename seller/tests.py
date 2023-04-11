from msilib.schema import SelfReg
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class TestSample(TestCase):

    def setup(self):
        self.client = APIClient

    def test_index(self):
        url = reverse('seller:index')
        res = self.client.get(url)
        self.assertEquals(res.data,'congratulations...... you have created an API')
        print(res.data)

    def test_number(self):
         url = reverse('seller:number')
         res = self.client.get(url)
         self.assertEqual(res.data,10)

        


