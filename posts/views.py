import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import resolve_url
from django.db.models import Q
from django.views.generic.edit import ModelFormMixin

from posts.models import Post
from django.urls import reverse_lazy
from django.views import generic
from posts.forms import (
    PostCreateForm,
    PostUpdateForm,

)


class PostCreateView(generic.CreateView, LoginRequiredMixin):  # 投稿機能
    model = Post
    template_name = 'post/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.master_username = self.request.user
        return super().form_valid(form)




class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/post_edit.html'

    def get_success_url(self):
        return resolve_url('post_detail', pk=self.kwargs['pk'])


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = '/'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'



# E-スポーツ関係


class FortniteDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/fortnite_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        elif q_data:
            object_list = Post.objects.filter(
                Q(event_date__icontains=q_data)
            )
        else:
            object_list = Post.objects.filter(e_sport_detail="10").order_by('event_date')
        return object_list.filter(e_sport_detail="10").order_by('event_date')


class ApexDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/apex_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        elif q_data:
                object_list = Post.objects.filter(
                    Q(event_date__icontains=q_data)
                )
        else:
            object_list = Post.objects.filter(e_sport_detail="20").order_by('event_date')
        return object_list.filter(e_sport_detail="20").order_by('event_date')

class MonhanDetailView(generic.ListView):
        model = Post
        template_name = 'post/e_sport/Monhan_detail.html'
        context_object_name = 'posts'

        def get_queryset(self):
            q_word = self.request.GET.get('query')
            q_data = self.request.GET.get('data')
            if q_word:
                object_list = Post.objects.filter(
                    Q(title__icontains=q_word) | Q(title__icontains=q_word)
                )
            elif q_data:
                object_list = Post.objects.filter(
                    Q(event_date__icontains=q_data)
                )
            else:
                object_list = Post.objects.filter(e_sport_detail="30").order_by('event_date')
            return object_list.filter(e_sport_detail="30").order_by('event_date')

class PokemonDetailView(generic.ListView):
        model = Post
        template_name = 'post/e_sport/Pokemon_detail.html'
        context_object_name = 'posts'

        def get_queryset(self):
            q_word = self.request.GET.get('query')
            q_data = self.request.GET.get('data')
            if q_word:
                object_list = Post.objects.filter(
                    Q(title__icontains=q_word) | Q(title__icontains=q_word)
                )
            elif q_data:
                object_list = Post.objects.filter(
                    Q(event_date__icontains=q_data)
                )
            else:
                object_list = Post.objects.filter(e_sport_detail="40").order_by('event_date')
            return object_list.filter(e_sport_detail="40").order_by('event_date')


class GuraburuDetailView(generic.ListView):
        model = Post
        template_name = 'post/e_sport/Guraburu_detail.html'
        context_object_name = 'posts'

        def get_queryset(self):
            q_word = self.request.GET.get('query')
            q_data=self.request.GET.get('data')
            if q_word:
                object_list = Post.objects.filter(
                    Q(title__icontains=q_word) | Q(title__icontains=q_word)
                )
            elif q_data:
                object_list = Post.objects.filter(
                    Q(event_date__icontains=q_data)
                )
            else:
                object_list = Post.objects.filter(e_sport_detail="50").order_by('event_date')
            return object_list.filter(e_sport_detail="50").order_by('event_date')


