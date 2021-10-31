from rest_framework import serializers

from .models import Customer, Product


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'city', 'tax_id', 'phone']

    id = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'inventory', 'purchase_price', 'unit_price']

    # This is to make id not required when creating or updating a product
    id = serializers.IntegerField(read_only=True)
