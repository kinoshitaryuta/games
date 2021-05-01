from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import resolve_url
from django.db.models import Q
from django.views.generic.edit import ModelFormMixin
from social_django.models import UserSocialAuth
from posts import api
from posts.models import Post,EventScheduleApex,EventScheduleMonhan,EventScheduleFortnite,EventScheduleGuraburu,Report
from django.urls import reverse_lazy
from django.views import generic
from posts.forms import (
    PostCreateForm,
    PostUpdateForm,
    ReportForm
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

class ReportView(generic.CreateView,LoginRequiredMixin):
    template_name = 'post/report_post.html'
    model = Report
    form_class = ReportForm


    def form_valid(self, form ):
        form.instance.author = self.request.user
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('post_detail',pk=post_pk)

# E-スポーツ関係


class FortniteDetailView(generic.ListView):
    model = Post
    template_name = 'post/e_sport/fortnite_detail.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['EventScheduleFortnite'] = EventScheduleFortnite.objects.all
        return context

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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['EventScheduleApex'] = EventScheduleApex.objects.all
        return context

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

        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context['EventScheduleMonhan'] = EventScheduleMonhan.objects.all
            return context


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


class GuraburuDetailView(generic.ListView):
        model = Post
        template_name = 'post/e_sport/Guraburu_detail.html'
        context_object_name = 'posts'

        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context['EventScheduleGuraburu'] = EventScheduleGuraburu.objects.all
            return context

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
                object_list = Post.objects.filter(e_sport_detail="40").order_by('event_date')
            return object_list.filter(e_sport_detail="40").order_by('event_date')


def search_tweets_guraburu(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        count   = request.POST['count']
        tweets = ''
        #ログインユーザーによって取得する値を変更する為、後日下記情報DBから取得出来るように変更
        oauth_session_params = {}
        oauth_session_params['consumer_key']    = 'EsiRDzxXVskEEjbtSwMkaaNxs'
        oauth_session_params['consumer_secret'] = '0UX5HSEeyk3obzYnKU904aEeIkZI8Qe4AJX5eHdH4yMFMjE19z'
        oauth_session_params['access_token']    = '1225787238224547840-5gt8RXlSr2WvH1cKZ0FlB7K286Yr4t'
        oauth_session_params['access_secret']   = 'UmHU6m7L5zERoz6sHTy09JorsmZKNOQl3a62zu9KQRmLb'
        #--------------------------------------
        twitterApi = api.TwitterApi(oauth_session_params)
        tweets = twitterApi.get_tweets(keyword, count)
    else:
        keyword = '参戦ID','参加者募集'
        count   = 10
        tweets  = ''
    context = {
        'keyword': keyword,
        'count'  : count,
        'tweets' : tweets,
    }
    return render(request, 'post/e_sport/tweets_Guraburu.html', context)

def search_tweets_monhan(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        count   = request.POST['count']
        tweets = ''
        #ログインユーザーによって取得する値を変更する為、後日下記情報DBから取得出来るように変更
        oauth_session_params = {}
        oauth_session_params['consumer_key']    = 'EsiRDzxXVskEEjbtSwMkaaNxs'
        oauth_session_params['consumer_secret'] = '0UX5HSEeyk3obzYnKU904aEeIkZI8Qe4AJX5eHdH4yMFMjE19z'
        oauth_session_params['access_token']    = '1225787238224547840-5gt8RXlSr2WvH1cKZ0FlB7K286Yr4t'
        oauth_session_params['access_secret']   = 'UmHU6m7L5zERoz6sHTy09JorsmZKNOQl3a62zu9KQRmLb'
        #--------------------------------------
        twitterApi = api.TwitterApi(oauth_session_params)
        tweets = twitterApi.get_tweets(keyword, count)
    else:
        keyword = '#モンハンライズフレンド募集'
        count   = 10
        tweets  = ''
    context = {
        'keyword': keyword,
        'count'  : count,
        'tweets' : tweets,
    }
    return render(request, 'post/e_sport/tweets_Monhan.html', context)

def search_tweets_apex(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        count   = request.POST['count']
        tweets = ''
        #ログインユーザーによって取得する値を変更する為、後日下記情報DBから取得出来るように変更
        oauth_session_params = {}
        oauth_session_params['consumer_key']    = 'EsiRDzxXVskEEjbtSwMkaaNxs'
        oauth_session_params['consumer_secret'] = '0UX5HSEeyk3obzYnKU904aEeIkZI8Qe4AJX5eHdH4yMFMjE19z'
        oauth_session_params['access_token']    = '1225787238224547840-5gt8RXlSr2WvH1cKZ0FlB7K286Yr4t'
        oauth_session_params['access_secret']   = 'UmHU6m7L5zERoz6sHTy09JorsmZKNOQl3a62zu9KQRmLb'
        #--------------------------------------
        twitterApi = api.TwitterApi(oauth_session_params)
        tweets = twitterApi.get_tweets(keyword, count)
    else:
        keyword = '#apexフレンド募集'
        count   = 10
        tweets  = ''
    context = {
        'keyword': keyword,
        'count'  : count,
        'tweets' : tweets,
    }
    return render(request, 'post/e_sport/tweets_apex.html', context)

def search_tweets_fortnite(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        count   = request.POST['count']
        tweets = ''
        #ログインユーザーによって取得する値を変更する為、後日下記情報DBから取得出来るように変更
        oauth_session_params = {}
        oauth_session_params['consumer_key']    = 'EsiRDzxXVskEEjbtSwMkaaNxs'
        oauth_session_params['consumer_secret'] = '0UX5HSEeyk3obzYnKU904aEeIkZI8Qe4AJX5eHdH4yMFMjE19z'
        oauth_session_params['access_token']    = '1225787238224547840-5gt8RXlSr2WvH1cKZ0FlB7K286Yr4t'
        oauth_session_params['access_secret']   = 'UmHU6m7L5zERoz6sHTy09JorsmZKNOQl3a62zu9KQRmLb'
        #--------------------------------------
        twitterApi = api.TwitterApi(oauth_session_params)
        tweets = twitterApi.get_tweets(keyword, count)
    else:
        keyword = '#フォートナイトフレンド募集'
        count   = 10
        tweets  = ''
    context = {
        'keyword': keyword,
        'count'  : count,
        'tweets' : tweets,
    }
    return render(request, 'post/e_sport/tweets_fortnite.html', context)