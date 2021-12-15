

from django.urls import path
from django.views.generic.edit import UpdateView

from products.views import (
    product_list, delete_product,
    create_product, product_detail, update_product, generate_form,
    create_product_form,
    ProductList, CreateProduct,
    AboutView,
    ProductListView,
    CreateProductView,
    ProductUpdateView
)
from django.views.generic.base import TemplateView


app_name = 'products'

# /products/products/
urlpatterns = [
    path("", ProductListView.as_view(), name='list'),
    path("delete/<int:product_id>/", delete_product, name='delete'),
    path("create/", create_product, name='create'),
    path("create/form/", CreateProductView.as_view(), name='create-form'),
    path("<int:product_id>/", product_detail, name='detail'),
    path("update/<int:product_id>/", update_product, name='update'),
    path("forms/<int:pk>/", ProductUpdateView.as_view()),
    path("about/", TemplateView.as_view(template_name="about.html"))

]
