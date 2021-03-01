from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import resolve_url
from posts.forms import PostCreateForm,PostUpdateForm
from posts.models import Post
from django.urls import reverse_lazy
from django.views import generic



class PostCreateView(generic.CreateView,LoginRequiredMixin):#投稿機能
    model = Post
    template_name = 'post/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.master_username=self.request.user
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


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class PostUpdateView(OnlyYouMixin, generic.UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/post_edit.html'

    def get_success_url(self):
        return resolve_url('post_detail', pk=self.kwargs['pk'])

class PostDeleteView(OnlyYouMixin,generic.DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = '/'