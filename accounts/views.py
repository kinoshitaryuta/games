from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
LoginView,
)
from .forms import (
UserLoginForm,
UserCreateForm,
)

class LoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'
