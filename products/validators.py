from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from products.models import Product


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"A product with this title already exists: {value}")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')
