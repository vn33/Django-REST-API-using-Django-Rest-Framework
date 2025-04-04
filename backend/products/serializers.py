from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content', 
            'price', 
            'sale_price',
            'discount'
        ]
    def get_discount(self, obj):
        #obj here is the instance
        return obj.get_discount()