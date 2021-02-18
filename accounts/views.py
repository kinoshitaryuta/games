from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import render_to_string
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


User = get_user_model()


class LoginView(LoginView):
    """ログイン機能"""
    form_class = UserLoginForm
    template_name = 'account/login.html'


class TemporaryRegistrationView(generic.CreateView):
    """登録機能"""
    template_name = 'account/temporary_registration.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(LogoutView):
    """ログアウトページ"""
    template_name = 'account/logout.html'