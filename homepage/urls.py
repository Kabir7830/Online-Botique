from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.Display_Homepage),
    path("clothes/all", views.get_all_clothes),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
