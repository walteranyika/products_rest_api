from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "pk",
            "title",
            "description",
            "price",
            "sale_price",
            "my_discount"
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        # if not isinstance(obj, Product):
        #     return None
        print(obj.id)
        return obj.get_discount()
