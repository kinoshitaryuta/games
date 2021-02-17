from accounts.models import  User
from django.contrib.auth.forms import(
UserCreationForm,
AuthenticationForm,
)

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username", "user_id", 'email','profession','profile_img','self_introduction', 'password1', 'password2',
        ]
