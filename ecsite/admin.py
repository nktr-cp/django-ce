from django.contrib import admin
from .models import Product, ProductPicture, Order

class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'type', 'price', 'stock')

class ProductPicturesAdmin(admin.ModelAdmin):
   list_display = ('product', 'priority', 'picture')

class OrderAdmin(admin.ModelAdmin):
   list_display = ('user', 'total_price')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPicture, ProductPicturesAdmin)
admin.site.register(Order, OrderAdmin)
