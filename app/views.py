from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views import generic
from accounts.models import User
from app.forms import (
    ContactForm,
    UserUpdateForm,

)



class HomeView(generic.TemplateView):
    template_name = 'app/home.html'

class HelpView(generic.TemplateView):
    template_name = 'app/help.html'

class TermsOfServiceView(generic.TemplateView):
    template_name = 'app/terms.html'

class PrivacyView(generic.TemplateView):
    template_name = 'app/privacy.html'



class ContactView(generic.CreateView, LoginRequiredMixin):
    template_name = 'app/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.send_email()
        return super().form_valid(form)

class ContactResultView(generic.TemplateView,LoginRequiredMixin):
    template_name = 'app/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context



class MyPageView(LoginRequiredMixin,generic.DetailView,):
    template_name = 'app/my_page.html'
    model = User


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserUpdateView(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'app/my_page_edit.html'

    def get_success_url(self):
        return resolve_url('my_page', pk=self.kwargs['pk'])

