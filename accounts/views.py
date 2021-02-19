from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (
LoginView,
LogoutView,
)
from .forms import (
UserLoginForm,
UserCreateForm,
)

class LoginView(LoginView):
    """ログイン機能"""
    form_class = UserLoginForm
    template_name = 'account/login.html'


class SignupView(generic.CreateView):
    """登録機能"""
    template_name = 'account/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('signup_text')

    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class SignupTextView(generic.TemplateView):
    template_name = 'account/signup_text.html'


class LogoutView(LogoutView):
    """ログアウトページ"""
    template_name = 'account/logout.html'