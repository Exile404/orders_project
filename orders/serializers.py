from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'total_amount', 'payment_status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.save()

        for item_data in items_data:
            item_id = item_data.get('id')
            if item_id:
                item = OrderItem.objects.get(id=item_id, order=instance)
                item.product_id = item_data.get('product_id', item.product_id)
                item.quantity = item_data.get('quantity', item.quantity)
                item.price = item_data.get('price', item.price)
                item.save()
            else:
                OrderItem.objects.create(order=instance, **item_data)

        return instance
