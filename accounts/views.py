from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.contrib.auth import get_user_model, login
from django.http import HttpResponseBadRequest
from django.contrib.auth.views import (
LoginView,
LogoutView,
)
from .forms import (
UserLoginForm,
UserCreateForm,
EmailChangeForm,
)

User = get_user_model()

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


class EmailChangeView(LoginRequiredMixin, generic.FormView):
    """メールアドレスの変更"""
    template_name = 'account/email_change_form.html'
    form_class = EmailChangeForm

    def form_valid(self, form):
        user = self.request.user
        new_email = form.cleaned_data['email']

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(new_email),
            'user': user,
        }

        subject = render_to_string('account/mails/subject.txt', context)
        message = render_to_string('account/mails/message.txt', context)
        send_mail(subject, message, None, [new_email])

        return redirect('email_change_done')


class EmailChangeDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/email_change_done.html'



class EmailChangeCompleteView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/email_change_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            new_email = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            User.objects.filter(email=new_email, is_active=False).delete()
            request.user.email = new_email
            request.user.save()
            return super().get(request, **kwargs)