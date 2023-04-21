from django.urls import path

from . import views

urlpatterns = [
    path("login", views.Login_Handler),
    path("logout", views.Logout_Handler),
    path("signup", views.New_Customer),
    path("<int:user_id>", views.Edit_User_Details),
    path("cart", views.get_cart_products),
    path("orders", views.get_all_user_orders),
    path("subscribe", views.subscribe_customer),
]
