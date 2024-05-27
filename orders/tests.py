from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Order, OrderItem
from decimal import Decimal

class OrderTests(APITestCase):
    
    def setUp(self):
        # Setup some initial data for testing
        self.order_data = {
            "user_id": 1,
            "total_amount": "100.00",
            "payment_status": "Pending",
            "items": [
                {"product_id": 1, "quantity": 2, "price": "50.00"}
            ]
        }
        
        self.order = Order.objects.create(user_id=1, total_amount="100.00", payment_status="Pending")
        self.order_item = OrderItem.objects.create(order=self.order, product_id=1, quantity=2, price="50.00")

    def test_create_order(self):
        url = reverse('order-list')
        response = self.client.post(url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(OrderItem.objects.count(), 2)
        
    def test_list_orders(self):
        url = reverse('order-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_order(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user_id'], self.order.user_id)

    def test_update_order(self):
        url = reverse('order-detail', args=[self.order.id])
        updated_data = {
            "user_id": 1,
            "total_amount": "150.00",
            "payment_status": "Completed",
            "items": [
                {"id": self.order_item.id, "product_id": 1, "quantity": 3, "price": "50.00"}
            ]
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.total_amount, Decimal("150.00"))
        self.assertEqual(self.order.payment_status, "Completed")
        self.assertEqual(self.order.items.first().quantity, 3)

    def test_partial_update_order(self):
        url = reverse('order-detail', args=[self.order.id])
        partial_data = {
            "total_amount": "120.00",
            "items": [
                {"id": self.order_item.id, "product_id": 1, "quantity": 4, "price": "30.00"}
            ]
        }
        response = self.client.patch(url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.total_amount, Decimal("120.00"))
        self.assertEqual(self.order.items.first().quantity, 4)
        self.assertEqual(self.order.items.first().price, Decimal("30.00"))

    def test_delete_order(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(OrderItem.objects.count(), 0)
