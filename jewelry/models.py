from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from autoslug import AutoSlugField


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    logo = models.ImageField(default=None)
    details = models.TextField(default=None)

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("jewelry:brand", kwargs={'slug': self.slug})


class Item(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    price = models.DecimalField(decimal_places=2, max_digits=7)
    brand = models.ForeignKey(Brand)
    img1 = models.ImageField(default=None)
    img2 = models.ImageField(default=None)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jewelry:item", kwargs={'brand': self.brand, 'slug': self.slug})
