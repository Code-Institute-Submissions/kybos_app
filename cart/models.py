from __future__ import unicode_literals
from django.db import models
from products.models import Terrarium
from django.contrib.auth.models import User

# Create your models here.

class cartItem(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Terrarium)
    quantity = models.IntegerField()

    def __str__(self):
        return "{0} ({1})".format(self.product.name, self.quantity)