from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from posts.forms import PostCreateForm
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
)
from posts.models import Post


class PostCreateView(CreateView,LoginRequiredMixin):#投稿機能
    model = Post
    template_name = 'post/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.username=self.request.user
        return super().form_valid(form)


class WorkDetailView(ListView):
    model = Post
    template_name = 'post/work_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(event_type="10")

class SportDetailView(ListView):
    model = Post
    template_name = 'post/sport_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(event_type="20")

class ESportDetailView(ListView):
    model = Post
    template_name = 'post/e_sport_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(event_type="30")

class HobbyDetailView(ListView):
    model = Post
    template_name = 'post/hobby_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(event_type="40")



