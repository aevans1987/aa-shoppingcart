"""App Configuration"""

# Django
from django.apps import AppConfig

# AA Example App
from shoppingcart import __version__


class ExampleConfig(AppConfig):
    """App Config"""

    name = "shoppingcart"
    label = "shoppingcart"
    verbose_name = f"AA-Shopping Cart app v{__version__}"
