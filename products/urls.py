

from django.urls import path

from products.views import product_list, delete_product

# /products/products/
urlpatterns = [
    path("", product_list),
    path("delete/<int:product_id>/", delete_product)
]
