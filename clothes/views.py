from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from customers.models import Customer_Clothes,Customer_Cart
from django.db.models import Q
from django.http import HttpResponseRedirect
def Add_Clothes(request):
    orders = Customer_Clothes.objects.filter(is_ordered = False)
    clothes_categories = Clothes_Categories.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        company = request.POST['company']
        size = request.POST['size']
        price = request.POST['price']
        color = request.POST['color']
        material = request.POST['material']
        photo1 = request.FILES['photo1']
        photo2 = request.FILES['photo2']
        photo3 = request.FILES['photo3']
        photo4 = request.FILES['photo4']
        photo5 = request.FILES['photo5']
        photo6 = request.FILES['photo6']
        category = request.POST['cloth_category']
        description = request.POST['description']

        try:
            Clothes.objects.create(
                name = name,
                company = company,
                size = size,
                price = price,
                color = color,
                material = material,
                photo1 = photo1,
                photo2 = photo2 if photo2 else "null",
                photo3 = photo3 if photo3 else "null",
                photo4 = photo4 if photo4 else "null",
                photo5 = photo5 if photo5 else "null",
                photo6 = photo6 if photo6 else "null",
                category_id = category,
                description = description
            )

            messages.success(request,"added")
            return redirect("/admin/clothes/add")
        except Exception as e:
            print(e)
            messages.error(request,"something went wrong!")
            return redirect("/admin/clothes/add")
    return render(request,"add_clothes.html",{"clothes_categories":clothes_categories,"orders_len":orders.count()})


def get_clothes(request):
    orders = Customer_Clothes.objects.filter(is_ordered = False)
    query = 0
    if request.GET.get('query'):
        query = request.GET.get('query')
    clothes = Clothes.objects.all()
    if query:
        clothes = Clothes.objects.filter(Q(name__icontains = query) | Q(company__icontains = query) | Q(material__icontains = query) | Q(category_id__category_name__icontains = query) | Q(price__icontains = query) | Q(color__icontains = query) | Q(size__icontains = query))
        
    return render(request,"user_clothes.html",{"clothes":clothes,"orders_len":orders.count(),"query":query})


def new_clothes_category(request):
    orders = Customer_Clothes.objects.filter(is_ordered = False)
    if request.method == "POST":
        try:
            category = Clothes_Categories.objects.create(
                category_name = request.POST['category_name']
            )
            messages.success(request,"created")
            return redirect("/clothes/new-category")
        except Exception as e:
            print(e)
            messages.error(request,"something went wrong!")
            return redirect("/clothes/new-category")
    return render(request,"add_category.html",{"orders_len":orders.count()})


def get_all_clothes(request):
    if request.user.is_superuser:
        clothes = Clothes.objects.all()
        return render(request,"all_clothes.html",{"clothes":clothes})
    

def delete_cloth(request,cloth_id):
    if request.method == "POST":
        cloth = Clothes.objects.filter(id = cloth_id).delete()
        messages.success(request,"deleted")
        return redirect("/admin/clothes/all")
    

def edit_clothes(request,cloth_id):
    cloth = Clothes.objects.filter(id = cloth_id)
    clothes_categories = Clothes_Categories.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        company = request.POST['company']
        size = request.POST['size']
        price = request.POST['price']
        color = request.POST['color']
        material = request.POST['material']
        photo = request.FILES.get('photo')
        category = request.POST['cloth_category']
        description = request.POST['description']
        print(photo)
        cloth.update(
            name = request.POST['name'] if request.POST['name'] else cloth.first().name, 
            company = company  if request.POST['company'] else cloth.first().company, 
            size = size  if request.POST['size'] else cloth.first().size, 
            price = price  if request.POST['price'] else cloth.first().price, 
            color = color  if request.POST['color'] else cloth.first().color, 
            material = material  if request.POST['material'] else cloth.first().material, 
            photo = photo  if request.FILES.get('photo') else cloth.first().photo, 
            category = category  if request.POST['cloth_category'] else cloth.first().category, 
            description = description  if request.POST['description'] else cloth.first().description, 
        )
        messages.success(request,"updated")
        return redirect(f"/admin/clothes/{cloth_id}/edit")
    return render(request,"edit_clothes.html",{"cloth":cloth.first(),"clothes_categories":clothes_categories})


def remove_from_cart(request,product_id):
    if not(request.user.is_authenticated):
        messages.warning(request,"login required!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        try:
            product = Customer_Cart.objects.filter(product_id = product_id).filter(customer_id = request.user.id).first().delete()
            messages.success(request,"removed from cart")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            print(e)
            messages.error(request,"something went wrong!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    