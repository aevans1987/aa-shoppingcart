"""
App Models
Create your models in here
"""

# Django
import timedate
from django.db import models
from django.utils import timezone
from allianceauth.authentication.models import CharacterOwnership
from allianceauth.eveonline.models import EveCharacter
from app_utils.django import users_with_permission

class General(models.Model):
    """Meta model for app permissions"""

    class Meta:
        """Meta definitions"""

        managed = False
        default_permissions = ()
        permissions = (("basic_access", "Can access this app"),
                       ["shopper", "Can take orders from the cart"])

class ShoppingCart(models.Model):
    timerequested = models.DateTimeField("Time Requested")
    requester = models.ForeignKey(
        EveCharacter
    )
    destination = models.CharField(
        max_length=20
    )
    janice_link = models.CharField(
        max_length=40
    )
    markup = models.FloatField(

    )
    shopper = models.ForeignKey(
        EveCharacter
    )