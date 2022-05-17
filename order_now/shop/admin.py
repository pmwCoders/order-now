from django.contrib import admin
from .models import (
    Product,
    Order,
    Order_product
)

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_product)
