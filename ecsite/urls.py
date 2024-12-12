from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView, CartView, AddToCartView, ConfirmOrderView

app_name = "ecsite"
urlpatterns = [
   path("home/", HomeView.as_view(), name="home"),
   path("list/", ProductListView.as_view(), name="list"),
   path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
   path("cart/", CartView.as_view(), name="cart"),
   path("add_to_cart/", AddToCartView.as_view(), name="add_to_cart"),
   path("confirm_order/", ConfirmOrderView.as_view(), name="confirm_order"),
]
