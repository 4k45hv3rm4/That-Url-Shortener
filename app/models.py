from django.db import models
from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com
# from django.urls import reverse
from django_hosts.resolvers import reverse

from django.conf import  settings


SHORTCODE_MAX  = getattr(settings, "SHORTCODE_MAX", 15)


class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = ShortURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by("-id")[:items]
        new_codes=0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class ShortURL(models.Model):

    url = models.CharField(max_length=220,validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)#when models was created
    updated = models.DateTimeField(auto_now=True)#set every time model is saved
    active = models.BooleanField(default=True)

    objects = ShortURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return self.url

    def __unicode__(self):
        return self.url

    def get_short_url(self):
        url_path = reverse("scode", kwargs = {'shortcode' : self.shortcode}, host="www", scheme="http")

        return  url_path
