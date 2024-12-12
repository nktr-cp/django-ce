from django.contrib import admin
from .models import Product, ProductPicture, Order, OrderItem, CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'stock')

class ProductPicturesAdmin(admin.ModelAdmin):
    list_display = ('product', 'priority', 'picture')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price')
    inlines = [OrderItemInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPicture, ProductPicturesAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem)