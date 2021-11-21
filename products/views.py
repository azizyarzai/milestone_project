from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required

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
    products = Product.objects.all()
    print(products.query)
    print(dir(request))
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'products-list.html', {'products': products})

    return redirect('/admin/login/')


def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id)
    product.delete()
    return redirect("/products/")


def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        product = Product.objects.create(
            name=name, price=price, quantity=quantity)
        product.save()
        return redirect("/products/")

    return render(request, 'create-product.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product-detail.html', {'product': product})
