

from django.urls import path

from products.views import product_list, delete_product, create_product, product_detail, update_product

app_name = 'products'

# /products/products/
urlpatterns = [
    path("", product_list, name='list'),
    path("delete/<int:product_id>/", delete_product, name='delete'),
    path("create/", create_product, name='create'),
    path("<int:product_id>/", product_detail, name='detail'),
    path("update/<int:product_id>/", update_product, name='update'),
]
