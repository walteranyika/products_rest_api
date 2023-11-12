from django.contrib import admin

# Register your models here.
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]


admin.site.register(Product, ProductAdmin)
