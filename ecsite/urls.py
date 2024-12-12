from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView

app_name = "ecsite"
urlpatterns = [
   path("home/", HomeView.as_view(), name="home"),
   path("list/", ProductListView.as_view(), name="list"),
   path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
]
