from django import forms
from django.contrib.auth import get_user_model

from .models import ChatBox


class SubmissionForm(forms.ModelForm):
    txt = forms.CharField(widget=forms.Textarea(attrs={'class': 'submission__message'}))

    class Meta:
        model = ChatBox
        fields = ('txt',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
