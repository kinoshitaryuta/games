from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from posts.forms import PostCreateForm
from posts.models import Post
from django.urls import reverse_lazy
from django.views import generic



class PostCreateView(generic.CreateView,LoginRequiredMixin):#投稿機能
    model = Post
    template_name = 'post/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.username=self.request.user
        return super().form_valid(form)


class WorkDetailView(generic.ListView):
    model = Post
    template_name = 'post/work_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(event_type="10")

class SportDetailView(generic.ListView):
    model = Post
    template_name = 'post/sport_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(event_type="20")

class ESportDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(event_type="30")

class HobbyDetailView(generic.ListView):
    model = Post
    template_name = 'post/hobby_detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(event_type="40")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'


