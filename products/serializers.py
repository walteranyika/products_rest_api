from rest_framework import serializers
from rest_framework.reverse import reverse

from main.serializers import UserPublicSerializer
from products.models import Product
from products.validators import validate_title


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title])
    owner = UserPublicSerializer(source='user', read_only=True)

    class Meta:
        model = Product
        fields = [
            "owner",
            "title",
            "description",
            "price",
            "sale_price",
            "my_discount",
            "url",
            "edit_url"
        ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"A product with this title already exists: {value}")
    #     return value

    # def create(self, validated_data):

    #     email = validated_data.pop("email")
    #     # Can do something with this email here
    #     obj = super().create(validated_data)
    #     return obj
    #
    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     return instance

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        # if not isinstance(obj, Product):
        #     return None
        print(obj.id)
        return obj.get_discount()
