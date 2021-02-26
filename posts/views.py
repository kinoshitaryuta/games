from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404, render
from posts.forms import PostCreateForm
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
)
from posts.models import Post


class PostCreateView(CreateView,LoginRequiredMixin):#投稿機能
    template_name = 'post/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.username=self.request.user
        return super().form_valid(form)

