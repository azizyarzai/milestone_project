

from django.urls import path

from products.views import product_list, delete_product, create_product, product_detail

# /products/products/
urlpatterns = [
    path("", product_list),
    path("delete/<int:product_id>/", delete_product),
    path("create/", create_product),
    path("<int:product_id>/", product_detail),
]
