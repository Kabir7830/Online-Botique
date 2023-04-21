from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import *


def New_Customer(request):
    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        age = request.POST['age']
        permanent_address = request.POST['permanent_address']
        resident_address = request.POST['resident_address']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        pin_code = request.POST['pin_code']

        user = Customers.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            age=age,
            permanent_address=permanent_address,
            resident_address=resident_address,
            country=country,
            state=state,
            city=city,
            pin_code=pin_code,
        )
        user.set_password(password)
        user.save()
        return Direct_Login(request, email=email, password=password)
    return render(request, "signup.html")


def Edit_User_Details(request, user_id):
    if request.method == "POST":
        user = Customers.objects.filter(id=user_id)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        age = request.POST['age']
        permanent_address = request.POST['permanent_address']
        resident_address = request.POST['resident_address']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        pin_code = request.POST['pin_code']

        user.update(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            age=age,
            permanent_address=permanent_address,
            resident_address=resident_address,
            country=country,
            state=state,
            city=city,
            pin_code=pin_code,
        )
        messages.success(request, "Details Updated")
        return redirect("/")
    return render(request, "edit_customer_details.html", {"customer": user})


def Login_Handler(request):
    if request.method == "POST":
        user = authenticate(
            email=request.POST['email'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            messages.success(request, "logged In")
            return redirect("/")
        messages.error(request, "Invalid email or password")
        return redirect("/")
    return render(request, "login.html")


def Logout_Handler(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "logged Out")
        return redirect("/")
    return redirect("/")


def Direct_Login(request, email, password):
    user = authenticate(
        email=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        messages.success(request, "User created and logged In")
        return redirect("/")


def add_to_cart(request, product_id):
    if not (request.user.is_authenticated):
        messages.warning(request, "login required!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        try:
            if Customer_Cart.objects.filter(product_id=product_id).filter(customer_id=request.user.id).exists():
                messages.warning(request, "product already in cart!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            cart = Customer_Cart.objects.create(
                customer_id_id=request.user.id,
                product_id_id=product_id
            )
            messages.success(request, "added to cart")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            print(e)
            messages.error(request, "something went wrong, try again!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def customer_orders(request, product_id):
    if not (request.user.is_authenticated):
        messages.warning(request, "login required!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        try:
            order = Customer_Orders.objects.create(
                customer_id_id=request.user.id,
                product_id_id=product_id,
                size=request.POST['size'],
                quantity=request.POST['quantity'],
            )
            messages.success(request, "order placed")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            print(e)
            messages.error(request, "something went wrong please try again!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_cart_products(request):
    if not (request.user.is_authenticated):
        messages.errro(request, "login required!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    clothes = Customer_Cart.objects.filter(customer_id=request.user.id)
    return render(request, "cart.html", {"clothes": clothes})


def get_all_user_orders(request):
    if not (request.user.is_authenticated):
        messages.errro(request, "login required!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    orders = Customer_Orders.objects.filter(customer_id=request.user.id)
    return render(request, "user_orders.html", {"orders": orders})


def subscribe_customer(request):
    if request.method == "POST":
        try:
            if Subscribe.objects.filter(customer_mail=request.POST['email']).exists():
                messages.warning(request, "already subscribed!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            subscribe_customer = Subscribe.objects.create(
                customer_mail=request.POST['email'],
                joining_date=request.POST['joining_date']
            )
            messages.success(request, "subscribed")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            print(e)
            messages.error(request, "something went wrong!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_all_subscribers(request):
    if not (request.user.is_superuser):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    subscribers = Subscribe.objects.all()
    return render(request, "subscribers.html", {"subscribers": subscribers})
