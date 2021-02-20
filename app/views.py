from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from app.forms import ContactForm



class HomeView(generic.TemplateView):
    template_name = 'app/home.html'

class HelpView(generic.TemplateView):
    template_name = 'app/help.html'


class ContactView(generic.CreateView, LoginRequiredMixin):
    template_name = 'app/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.send_email()
        return super().form_valid(form)


class ContactResultView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'app/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context


