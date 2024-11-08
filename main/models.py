from django.db import models

from io import BytesIO
from django.core.files import File
from django.utils import timezone

from main.choices import *

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import secrets
import uuid


# @receiver(pre_save, sender=User)
# def set_new_user_inactive(sender, instance, **kwargs):
#     if instance._state.adding is True:
#         instance.is_active = False


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         Wallet.objects.create(user=instance)
#         instance.profile.save()
#         instance.wallet.save()


