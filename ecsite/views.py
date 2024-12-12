from django.views.generic import TemplateView, ListView
from .models import Product

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
