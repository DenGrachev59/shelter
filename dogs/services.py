from django.conf import settings
from django.core.cache import cache

from dogs.models import Category


def get_categories_cache():
    if settings.CACHE_ENABLED:

        key = 'category_list'  # ключ по которому будут лежать данные в кеше
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
        else:
            category_list = Category.objects.all()

    return  category_list