
from django.contrib import admin
from django.urls import path,include
from customers.views import get_all_subscribers
from clothes.views import Add_Clothes,new_clothes_category,get_all_clothes,delete_cloth,edit_clothes
from homepage.views import Display_Admin_Dashboard,get_orders,make_orders_read,delete_orders

urlpatterns = [
    path('d-admin/', admin.site.urls),
    path('', include("homepage.urls")),
    path('customers/', include("customers.urls")),
    path('clothes/', include("clothes.urls")),
    path('admin/clothes/add', Add_Clothes),
    path('admin/clothes/new-category', new_clothes_category),
    path('admin/orders', get_orders),
    path('admin/orders/<int:order_id>', make_orders_read),
    path('admin/orders/<int:order_id>/delete', delete_orders),
    path('admin/clothes/all', get_all_clothes),
    path('admin/clothes/<int:cloth_id>/delete', delete_cloth),
    path('admin/clothes/<int:cloth_id>/edit', edit_clothes),
    path('admin/subscribers', get_all_subscribers),

]
