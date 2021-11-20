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
    print(dir(request))
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'products-list.html', {'products': products})

    return redirect('/admin/login/')


def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id)
    product.delete()
    return redirect("/products/")
