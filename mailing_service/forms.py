from django import forms

from mailing_service.models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        # fields = ('first_name', 'last_name', 'email')
        fields = '__all__'

