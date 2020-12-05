from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import ChatBox

class ChatAdd(forms.ModelForm):
    txt = forms.CharField(widget=forms.Textarea(attrs={'class': 'submission__message'}))

    class Meta:
        model = ChatBox
        fields = ('txt',)