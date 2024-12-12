from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Product, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HomeView(TemplateView):
   template_name = "ecsite/shophome.html"

class ProductListView(ListView):
   model = Product
   template_name = "ecsite/list.html"
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       product = Product.objects.all()
       context["cakes"] = product.filter(type="cakes")
       context["bakedcakes"] = product.filter(type="bakedcakes")
       context["goods"] = product.filter(type="goods")
       return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "ecsite/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            user = self.request.user
            mycartitem = CartItem.objects.filter(user_id=user).values_list("product_id", flat=True)
            context["cart_contents"] = Product.objects.filter(id__in=mycartitem)
        return context

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import CartItem
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
class CartView(View):
    def get(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)
        total_price = sum(item.qty * item.product.price for item in cart_items)
        for item in cart_items:
            item.total_price = item.qty * item.product.price
            print(item.total_price)
        return render(request, 'ecsite/cart.html', {'cart_items': cart_items, 'total_price': total_price})

    def post(self, request):
        item_id = request.POST.get('item_id')
        action = request.POST.get('action', 'update')
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

        if action == 'delete':
            cart_item.delete()
            messages.success(request, "商品がカートから削除されました。")
        else:
            qty = request.POST.get('qty')
            if qty and qty.isdigit() and int(qty) > 0:
                cart_item.qty = int(qty)
                cart_item.save()
                messages.success(request, "数量が更新されました。")
            else:
                messages.error(request, "数量は正の整数でなければなりません。")

        return redirect('ecsite:cart')

class AddToCartView(View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        qty = request.POST.get("qty")
        if not qty or not qty.isdigit() or int(qty) <= 0:
            messages.error(request, "数量は正の整数でなければなりません。")
            return redirect("ecsite:detail", pk=product_id)
        qty = int(qty)
        product = get_object_or_404(Product, id=product_id)
        user = request.user
        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.qty += qty
        else:
            cart_item.qty = qty
        cart_item.save()
        return redirect("ecsite:cart")

@method_decorator(login_required, name="dispatch")
class ConfirmOrderView(View):
    def post(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)
        if not cart_items.exists():
            messages.error(request, "カートに商品がありません。")
            return redirect("ecsite:cart")
        total_price = sum(item.qty * item.product.price for item in cart_items)
        order = Order.objects.create(user=user, total_price=total_price)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, qty=item.qty)
            # Reduce the product quantity
            item.product.stock -= item.qty
            item.product.save()
        cart_items.delete()
        return render(request, "ecsite/confirm_order.html", {"order": order})
