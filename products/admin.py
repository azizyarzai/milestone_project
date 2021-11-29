from django.contrib import admin
from products.models import Product, Distributer

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'created', 'updated']
    list_display_links = ['id', 'name']
    list_filter = ['created', 'price']
    list_per_page = 5
    search_fields = ['name', 'price']


admin.site.register(Product, ProductAdmin)

admin.site.register(Distributer)
