from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Event(models.Model):
    event = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='event')
    start = models.DateField()
    end = models.DateField()
    details = models.TextField(max_length=2000)
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse('events:details', kwargs={'pk': self.pk})

    def __str__(self):
        if self.start == self.end:
            return self.event + '  on  ' + self.end.strftime("%B %d %Y")
        else:
            return self.event + '   ' + self.start.strftime("%B %d %Y") + ' - ' + self.end.strftime("%B %d %Y")

    class Meta:
        ordering = ['start']
