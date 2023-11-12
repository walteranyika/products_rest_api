from django.urls import path

from products import views

urlpatterns = [
    # path('<int:pk>', views.ProductDetailApiView.as_view()),
    path('', views.product_list_create_view, name="product-list"),
    path('<int:pk>/update', views.product_update_view, name="product-edit"),
    path('<int:pk>/delete', views.product_destroy_view),
    path('<int:pk>', views.product_detail_view, name="product-detail"),
    # path('mixins', views.product_mixin_view),
    # path('mixins/<int:pk>', views.product_mixin_view),

]
