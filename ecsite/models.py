from django.db import models
from accounts.models import CustomUser

class Product(models.Model):
   Cakes = 'cakes'
   BakedCakes = 'bakedcakes'
   Goods = 'goods'
   TYPE = [
       (Cakes, '生菓子'),
       (BakedCakes, '焼き菓子'),
       (Goods, '備品'),
   ]
   name = models.CharField(max_length=50, verbose_name='商品名')
   type = models.CharField(max_length=20, verbose_name='種類', choices=TYPE)
   price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='価格')
   stock = models.PositiveIntegerField(default=0, verbose_name='在庫')  # Ensure stock is a positive integer
   comments = models.CharField(max_length=100, verbose_name='商品説明')
   size = models.CharField(max_length=50, verbose_name='サイズ')
   campaign = models.CharField(max_length=100, verbose_name='キャンペーン説明', blank=True, null=True)
   ingredients = models.CharField(max_length=50, verbose_name='原材料')
   class Meta:
       db_table = 'products'
   def __str__(self):
       return self.name
   def save(self, *args, **kwargs):
       if self.stock < 0:
           raise ValueError("Stock cannot be negative")
       super().save(*args, **kwargs)

class ProductPicture(models.Model):
   picture = models.FileField(upload_to='product_pictures')
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   priority = models.IntegerField()
   class Meta:
       db_table = 'product_pictures'
       ordering = ['priority']
       # 画像の優先順位が重複しないように制約を追加
       constraints = [
           models.UniqueConstraint(fields=['product', 'priority'], name='picture_priority')
       ]
   def __str__(self):
       return self.product.name + ':' + str(self.priority)

class CartItem(models.Model):
   qty = models.PositiveIntegerField(default=1)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   user = models.ForeignKey(
       CustomUser, on_delete=models.CASCADE
   )
   class Meta:
       db_table = 'cart_items'
       constraints = [
           models.UniqueConstraint(fields=['product', 'user'], name='incart_product')
       ]


class Order(models.Model):
   total_price = models.PositiveIntegerField()
   user = models.ForeignKey(
       CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
   class Meta:
       db_table = 'orders'
       

class OrderItem(models.Model):
   qty = models.PositiveIntegerField()
   product = models.ForeignKey(
       Product, on_delete=models.SET_NULL, blank=True, null=True)
   order = models.ForeignKey(
       Order, on_delete=models.CASCADE, blank=True, null=True)
   class Meta:
       db_table = 'order_items'
       constraints = [
           models.UniqueConstraint(fields=['product', 'order'], name='order_constrain')
       ]
