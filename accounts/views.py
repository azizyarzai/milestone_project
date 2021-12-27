from django.shortcuts import redirect, render
from django.contrib.auth import login, get_user_model, authenticate, logout
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
    if request.method == "GET":
        return render(request, 'accounts/register.html')

    email = request.POST.get("email")
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    dob = request.POST.get("dob")
    password = request.POST.get("password")

    try:
        user = get_user_model().objects.get(email=email)
        messages.error(request, "This email already exists.")
        return redirect("/accounts/register/")

    except:
        user = get_user_model().objects.create_user(email=email, name=name,
                                                    gender=gender, date_of_birth=dob, password=password)
        login(request, user)
        messages.success(request, "You are registed successfuly.")
        return redirect("/products/")


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You are logged out successfuly.")
        return redirect("/products/")
