import random

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from clothes.models import Clothes
from customers.models import Customer_Clothes, Customer_Orders

# Create your views here.


def Display_Homepage(request):
    trending_clothes = Clothes.objects.all()
    sarees = Clothes.objects.filter(category__category_name="saree")
    kurtas = Clothes.objects.filter(category__category_name="kurta")
    if sarees.count() > 2:
        sarees = random.sample(list(sarees), 3)
    counter = list(range(1, 7))
    if kurtas.count() > 2:
        kurtas = random.sample(list(kurtas), 3)
    counter = list(range(1, 7))
    return render(request, "index.html", {"trending_clothes": random.sample(list(trending_clothes), 3), "counter": counter, "sarees": sarees, "kurtas": kurtas})


def Display_Admin_Dashboard(request):
    if request.user.is_superuser:
        orders = Customer_Clothes.objects.filter(is_ordered=False)
        return render(request, "admin.html", {"order_len": len(orders)})
    return HttpResponse("bad request")


def buy_now(request, product_id):
    product = Clothes.objects.filter(id=product_id)
    photos = []
    for pic in product:
        photos.append(pic.photo2)
        photos.append(pic.photo3)
        photos.append(pic.photo4)
        photos.append(pic.photo5)
        photos.append(pic.photo6)
    print(len(photos))
    print(photos)
    return render(request, "buy_now.html", {"product": product.first(), "photos": photos})


def get_orders(request):
    orders = Customer_Orders.objects.all()
    return render(request, "orders.html", {"orders": orders})


def make_orders_read(request, order_id):
    if request.method == "POST":
        order = Customer_Orders.objects.filter(id=order_id).update(
            is_ordered=True,
        )
        messages.success(request, "marked ordered")
        return redirect("/admin/orders")


def delete_orders(request, order_id):
    if request.method == "POST":
        order = Customer_Orders.objects.filter(id=order_id).delete()
        messages.success(request, "order deleted")
        return redirect("/admin/orders")


def get_all_clothes(request):
    clothes = Clothes.objects.all()
    return render(request, "user_clothes.html", {"clothes": clothes})
