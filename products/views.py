from django.contrib import messages
from django.views.generic.base import View
from products.forms import ProductModelForm
from products.forms import StudentForm
from django.db.models import Q
from django.http.response import Http404, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
from products.models import Product, Distributer


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'is_availible',
              'image', 'user', 'distributers', 'category']
    template_name = 'products/form.html'

    # def get_queryset(self):
    #     print("id:", self.kwargs.get("product_id"))
    #     return Product.objects.get(id=self.kwargs.get("product_id"))


class AboutView(TemplateView):
    template_name = 'about.html'


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
    return render(request, 'products/index.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = {}
        no_product = Product.objects.all().count()
        context['no_product'] = no_product
        return context


class ProductList(View):
    def get(self, request):
        products = Product.objects.filter(
            Q(is_availible=True) | Q(quantity__gte=28))
        print(products.query)
        # print(dir(request))
        # print(request.user)
        if request.user.is_authenticated:
            return render(request, 'products/products-list.html', {'products': products})

        return redirect('/admin/login/')


def product_list(request):
    # products = Product.objects.filter(is_availible=True, quantity__gte=28)
    products = Product.objects.filter(
        Q(is_availible=True) | Q(quantity__gte=28))
    print(products.query)
    # print(dir(request))
    # print(request.user)
    if request.user.is_authenticated:
        return render(request, 'products/products-list.html', {'products': products})

    return redirect('/admin/login/')


def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        messages.success(request, "Product Deleted Successfuly.")
        messages.error(request, "Something  went wrong.")
    except Product.DoesNotExist:
        raise Http404()
    except Product.MultipleObjectsReturned:
        return HttpResponse("More than object returned.")

    print(reverse_lazy('products:list'))
    return redirect(reverse_lazy('products:list'))


class CreateProductView(CreateView):
    model = Product
    template_name = 'products/create-product-form.html'
    fields = ['name', 'price', 'quantity', 'is_availible',
              'image', 'user', 'distributers', 'category']


class CreateProduct(View):
    def get(self, request):
        product_form = ProductModelForm(initial={'name': "Amin"})
        return render(request, 'products/create-product-form.html', {'form': product_form})

    def post(self, request):
        product_form = ProductModelForm(request.POST)
        if product_form.is_valid():
            print(product_form.cleaned_data)
            product_form.save()
        return render(request, 'products/create-product-form.html', {'form': product_form})


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

    return render(request, 'products/create-product.html')


def product_detail(request, product_id):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except Product.DoesNotExist:
    #     raise Http404()

    product = get_object_or_404(Product, id=product_id)
    print(dir(product.user))
    return render(request, 'products/product-detail.html', {'product': product})


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
    return render(request, 'products/update-product.html', {"product": product})


def generate_form(request):
    student_form = StudentForm(request.POST or None)
    if request.method == "POST" and student_form.is_valid():
        print(student_form.cleaned_data.get('roll_no'))
        return HttpResponse("Valid data")

    return render(request, 'products/form.html', {'form': student_form})


def create_product_form(request):
    product_form = ProductModelForm(initial={'name': "Amin"})
    if request.method == "POST" and product_form.is_valid():
        print(product_form.cleaned_data)
        product_form.save()
    return render(request, 'products/create-product-form.html', {'form': product_form})
