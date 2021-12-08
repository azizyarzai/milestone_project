from django.contrib import admin
from products.models import Product, Distributer

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price',
                    'quantity', 'created', 'updated', 'added_on']
    list_display_links = ['id', 'name']
    list_filter = ['created', 'price']
    list_per_page = 5
    search_fields = ['name', 'price']
    # exclude = ['slug']
    fields = ['name', 'price',
              'quantity', 'user', 'distributers',
              'category', 'is_availible', 'image', 'created', 'updated', 'added_on']

    readonly_fields = ['created', 'updated', 'added_on']

    class Meta:
        readonly_fields = ['slug']


admin.site.register(Product, ProductAdmin)

admin.site.register(Distributer)
