from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Terrarium(models.Model):
    SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('B', 'Big')
    )
    COLORS = (
        ('S', 'Silver'),
        ('M' ,'Bronce'),
        ('B', 'Black')
    )
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    price_small = models.DecimalField(max_digits=100, decimal_places=2)
    price_medium = models.DecimalField(max_digits=100, decimal_places=2)
    price_big = models.DecimalField(max_digits=100, decimal_places=2)
    size = models.CharField(max_length=1, choices=SIZE, default=1)
    colors = models.CharField(max_length=1, choices=COLORS, default=1 )
    cover = models.ImageField(upload_to='images')
    cover_main = models.ImageField(upload_to='images')
    img_one = models.ImageField(upload_to='images')
    img_two = models.ImageField(upload_to='images')
    img_three = models.ImageField(upload_to='images')
    img_four = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

