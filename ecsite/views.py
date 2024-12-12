from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, CartItem

class HomeView(TemplateView):
   template_name = 'ecsite/shophome.html'

class ProductListView(ListView):
   model = Product
   template_name = 'ecsite/list.html'
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       product = Product.objects.all()
       context['cakes'] = product.filter(type='cakes')
       context['bakedcakes'] = product.filter(type='bakedcakes')
       context['goods'] = product.filter(type='goods')
       return context

class ProductDetailView(DetailView):
   model = Product
   template_name = 'ecsite/detail.html'
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       if self.request.user.is_anonymous:
           pass
       else:
           user = self.request.user
           mycartitem = (CartItem.objects.filter(user_id=user)).values_list('product_id')
           context['cart_contents'] = Product.objects.filter(id__in=mycartitem)
       return context
