from django import forms
from django.forms import ModelForm

from accounts.models import User
from app.models import Contact
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

from posts.models import Post


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [

       'contact_us','email','message','username'
        ]

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        email = self.cleaned_data['email']
        from_email = ' <{email}>'.format( email=email)
        recipient_list = [settings.EMAIL_HOST_USER]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username','self_introduction'
        ]


