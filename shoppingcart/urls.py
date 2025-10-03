"""App URLs"""

# Django
from django.urls import path

# AA Example App
from shoppingcart import views

app_name: str = "shoppingcart"

urlpatterns = [
    path("", views.index, name="index"),
]
