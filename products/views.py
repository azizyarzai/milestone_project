from django.shortcuts import render, HttpResponse

# Create your views here.


def get_users(request):
    print(type(request))
    print('get_users called.')
    return HttpResponse("<h1>Welcome to django</h1>")


def home(request):
    a = 5
    b = 12
    res = a * b

    context = {
        'data': res
    }
    return render(request, 'index.html', context)
