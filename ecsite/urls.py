from django.urls import path
from .views import HomeView, ProductListView

app_name = "ecsite"
urlpatterns = [
   path("home/", HomeView.as_view(), name="home"),
   path("list/", ProductListView.as_view(), name="list"),
]
