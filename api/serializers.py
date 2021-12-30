from rest_framework import serializers

from products.models import Product


class TestSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=5)
    age = serializers.IntegerField(required=False)
    address = serializers.CharField(max_length=10)


class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['slug', ]
        read_only_fields = ['id', 'created', 'updated']
