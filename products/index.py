from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from products.models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public' # Will this go to algolia or not
    fields = [
        'title',
        'description',
        'price',
        'user',
        'public',
    ]
    settings = {
        'searchableAttributes': ['title', 'description'],
        'attributesForFaceting': ['user', 'public']
    }
    tags = 'get_tags_list'
