from django.conf import settings
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query=None, user=None):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self.db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=1, null=True)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "12"
