from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
from products.models import Product


def get_users(request):
    print(type(request))
    print('get_users called.')
    return HttpResponse("<h1>Welcome to django</h1>")


# @login_required(login_url="/test/")
def home(request):
    a = 5
    b = 12
    res = a * b

    context = {
        'data': res
    }
    return render(request, 'index.html', context)


def product_list(request):
    # products = Product.objects.filter(is_availible=True, quantity__gte=28)
    products = Product.objects.filter(
        Q(is_availible=True) | Q(quantity__gte=28))
    print(products.query)
    # print(dir(request))
    # print(request.user)
    if request.user.is_authenticated:
        return render(request, 'products-list.html', {'products': products})

    return redirect('/admin/login/')


def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id)
    product.delete()
    print(reverse_lazy('products:list'))
    return redirect(reverse_lazy('products:list'))


def create_product(request):
    # dic = {
    #     "name": "Ahamd",
    #     "age": 25
    # }
    # dic["age"]
    # dic.get("age", )
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        product = Product.objects.create(
            name=name, price=price, quantity=quantity)
        product.save()
        return redirect(reverse_lazy('products:list'))

    return render(request, 'create-product.html')


def product_detail(request, product_id):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except Product.DoesNotExist:
    #     raise Http404()

    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product-detail.html', {'product': product})


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        product.name = name
        product.price = price
        product.quantity = quantity
        product.save()
        return redirect(reverse_lazy('products:detail', kwargs={'product_id': product.id}))
    return render(request, 'update-product.html', {"product": product})
