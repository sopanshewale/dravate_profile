from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    address  = models.TextField(max_length=200)
    phone  = models.CharField(max_length=100)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        try:
             profile = Userprofile.objects.get(user_id=user.id)
             profile.save()
        except Userprofile.DoesNotExist:
             profile = Userprofile(user_id=user.id)
post_save.connect(create_profile, sender=User)


