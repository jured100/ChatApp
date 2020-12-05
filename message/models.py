from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class ChatBox(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='my_private_messages')
    txt = models.TextField(max_length=512)
    datum = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['datum']

    def __str__(self):
        return self.txt
