from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'city', 'tax_number', 'phone']

    id = serializers.IntegerField(read_only=True)
