from django.db import models
from app.models import ShortURL


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, ShortURL):
            obj, created = self.get_or_create(short_url = instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):

    short_url = models.OneToOneField(ShortURL, on_delete=models.CASCADE)
    count     = models.IntegerField(default=0)
    # timestamp = models.DateTimeField(auto_now_add=True)#when models was created
    # updated = models.DateTimeField(auto_now=True)#set every time model is saved

    objects   = ClickEventManager()

    def __str__(self):
        return "{url}-{i}".format(url = self.short_url,i =self.count)
