from django.shortcuts import redirect, render
from django.contrib.auth import login, get_user_model, authenticate
from django.contrib import messages
# Create your views here.


def login_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    email = request.POST.get("email")
    password = request.POST.get("password")

    # user = get_user_model().objects.get(email=email, password=password)
    user = authenticate(request, email=email, password=password)
    print(user)
    if user:
        login(request, user)
        messages.success(request, "You are logged in.")
        return redirect("/products/")

    messages.error(request, "Wrong credentials.")
    return render(request, 'accounts/login.html')


def register(request):
    pass
