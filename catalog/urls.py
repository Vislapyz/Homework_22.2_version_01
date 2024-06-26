from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    ContactsTemplateView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product/", ProductCreateView.as_view(), name="create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete"),
]
