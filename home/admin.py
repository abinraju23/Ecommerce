from django.contrib import admin
from .models import Product,ShoppingCart,Category

admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Category)