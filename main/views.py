from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response({"message": "Invalid Data"})
# @api_view(["GET", "POST"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#         data = ProductSerializer(instance).data
#     return Response(data)


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # data["id"] = model_data.id
#         # data["title"] = model_data.title
#         # data["content"] = model_data.description
#         # data["price"] = model_data.price
#         # serialization
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return JsonResponse(data)

# return HttpResponse(json, headers={"content-type": "application/json"})
