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


# class OnlyYouMixin(UserPassesTestMixin):
#     raise_exception = True
#
#     def test_func(self):
#         user = self.request.user
#         return user.pk == self.kwargs['pk'] or user.is_superuser


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


# work関係
class WorkDetailView(generic.TemplateView):
    template_name = 'post/work_detail.html'


class SeminarDetailView(generic.ListView):
    model = Post
    template_name = 'post/work/Seminar_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(work_detail="10").order_by('event_date')
        return object_list.filter(work_detail="10").order_by('event_date')


class ExchangeDetailView(generic.ListView):
    model = Post
    template_name = 'post/work/Exchange_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(work_detail="20").order_by('event_date')
        return object_list.filter(work_detail="20").order_by('event_date')


class BusinessCardDetailView(generic.ListView):
    model = Post
    template_name = 'post/work/business_card_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(work_detail="30").order_by('event_date')
        return object_list.filter(work_detail="30").order_by('event_date')


class StudentsDetailView(generic.ListView):
    model = Post
    template_name = 'post/work/students_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(work_detail="40").order_by('event_date')
        return object_list.filter(work_detail="40").order_by('event_date')


class OtherWorkDetailView(generic.ListView):
    model = Post
    template_name = 'post/work/other_work_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(work_detail="50").order_by('event_date')
        return object_list.filter(work_detail="50").order_by('event_date')


# スポーツ関係
class SportDetailView(generic.TemplateView):
    template_name = 'post/sport_detail.html'


class BeginnerDetailView(generic.ListView):
    model = Post
    template_name = 'post/sport/beginner_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(sport_detail="10").order_by('event_date')
        return object_list.filter(sport_detail="10").order_by('event_date')


class ExperiencedDetailView(generic.ListView):
    model = Post
    template_name = 'post/sport/experienced_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(sport_detail="20").order_by('event_date')
        return object_list.filter(sport_detail="20").order_by('event_date')


class WatchingGamesDetailView(generic.ListView):
    model = Post
    template_name = 'post/sport/watching_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(sport_detail="30").order_by('event_date')
        return object_list.filter(sport_detail="30").order_by('event_date')


class OtherSportDetailView(generic.ListView):
    model = Post
    template_name = 'post/sport/other_sport_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(sport_detail="40").order_by('event_date')
        return object_list.filter(sport_detail="40").order_by('event_date')


# E-スポーツ関係
class ESportDetailView(generic.TemplateView):
    template_name = 'post/e_sport_detail.html'


class FortniteDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/fortnite_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(e_sport_detail="10").order_by('event_date')
        return object_list.filter(e_sport_detail="10").order_by('event_date')


class PubgDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/pubg_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(e_sport_detail="20").order_by('event_date')
        return object_list.filter(e_sport_detail="20").order_by('event_date')


class ApexDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/apex_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(e_sport_detail="30").order_by('event_date')
        return object_list.filter(e_sport_detail="30").order_by('event_date')


class MinecraftDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/minecraft_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(e_sport_detail="40").order_by('event_date')
        return object_list.filter(e_sport_detail="40").order_by('event_date')


class LeagueDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/league_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(e_sport_detail="50").order_by('event_date')
        return object_list.filter(e_sport_detail="50").order_by('event_date')


class OtherESportDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/other_e_sport_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(e_sport_detail="60").order_by('event_date')
        return object_list.filter(e_sport_detail="60").order_by('event_date')


# 趣味関係
class HobbyDetailView(generic.TemplateView):
    template_name = 'post/hobby_detail.html'


class ReadBookDetailView(generic.ListView):
    model = Post
    template_name = 'post/hobby/read_book_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(hobby_detail="10").order_by('event_date')
        return object_list.filter(hobby_detail="10").order_by('event_date')


class SocialGatheringDetailView(generic.ListView):
    model = Post
    template_name = 'post/hobby/social_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(hobby_detail="20").order_by('event_date')
        return object_list.filter(hobby_detail="20").order_by('event_date')


class MorningActivityView(generic.ListView):
    model = Post
    template_name = 'post/hobby/morning_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(hobby_detail="30").order_by('event_date')
        return object_list.filter(hobby_detail="30").order_by('event_date')


class OtherHobbyDetailView(generic.ListView):
    model = Post
    template_name = 'post/hobby/other_hobby_detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word) | Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.filter(hobby_detail="40").order_by('event_date')
        return object_list.filter(hobby_detail="40").order_by('event_date')
