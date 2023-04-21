from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from homepage.views import buy_now
from customers.views import add_to_cart,customer_orders
urlpatterns = [
    # path("add",views.Add_Clothes),
    path("",views.get_clothes),
    # path("new-category",views.new_clothes_category),
    path("<int:product_id>/buy",buy_now),
    path("<int:product_id>/add-to-cart",add_to_cart),
    path("<int:product_id>/remove-from-cart",views.remove_from_cart),
    path("<int:product_id>/purchase",customer_orders),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
