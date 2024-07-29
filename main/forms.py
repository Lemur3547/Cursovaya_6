from django import forms

from main.models import Mailing, Client, Message
from users.forms import StyleFormMixin


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('user',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('name', 'first_mall', 'regularity', 'clients', 'message')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(user=user)
        self.fields['message'].queryset = Message.objects.filter(user=user)
