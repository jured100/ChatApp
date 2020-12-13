from django import forms
from django.contrib.auth.models import User

from .models import Message


class SubmissionForm(forms.ModelForm):
    txt = forms.CharField(widget=forms.Textarea(attrs={'class': 'submission__message'}))

    class Meta:
        model = Message
        fields = ('txt',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
