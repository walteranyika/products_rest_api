from rest_framework import generics, mixins

from main.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateApiView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description") or None
        if description is None:
            description = title
        serializer.save(user=self.request.user, description=description)
        # Send a django signal here

    def get_queryset(self):
        qs = super(ProductListCreateApiView, self).get_queryset()
        request = self.request
        print(request.user)
        return qs.filter(user=request.user)


product_list_create_view = ProductListCreateApiView.as_view()


class ProductDetailApiView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


product_detail_view = ProductDetailApiView.as_view()


class ProductListApiView(StaffEditorPermissionMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListApiView.as_view()


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()


product_update_view = ProductUpdateApiView.as_view()


class ProductDeleteApiView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


product_destroy_view = ProductDeleteApiView.as_view()


class ProductMixinView(StaffEditorPermissionMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


product_mixin_view = ProductMixinView.as_view()
