from django import forms
from accounts.models import User
from django.contrib.auth.forms import(
UserCreationForm,
AuthenticationForm,
)

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'email', 'password',
        ]
        labels = {
            'email': 'E-mail',
            'password': 'password',

        }


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username','email','self_introduction', 'password1', 'password2',
        ]

class EmailChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'email',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email