from django import forms
from .models import NotificationType


class NotificationForm(forms.Form):
    user = forms.CharField(label="User ID", max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    notification_type = forms.ModelChoiceField(queryset=NotificationType.objects.all())
