from django.db import models
from django.conf import settings
import os
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class ChatBox(models.Model):
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True, related_name='my_private_messages')
    txt=models.TextField(max_length=512)
    datum=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.txt
