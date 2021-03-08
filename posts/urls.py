from django.urls import path,include
from.import views


urlpatterns=[
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('work/', views.WorkDetailView.as_view(), name='work'),
    path('sport/', views.SportDetailView.as_view(), name='sport'),
    path('e-sport/', views.ESportDetailView.as_view(), name='e-sport'),
    path('hobby/', views.HobbyDetailView.as_view(), name='hobby'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),


    path('seminar/', views.SeminarDetailView.as_view(), name='seminar'),
    path('exchange/', views.ExchangeDetailView.as_view(), name='exchange'),
    path('business/', views.BusinessCardDetailView.as_view(), name='business'),
    path('students/', views.StudentsDetailView.as_view(), name='students'),
    path('other/work/', views.OtherWorkDetailView.as_view(), name='other_work'),

    path('beginner/', views.BeginnerDetailView.as_view(), name='beginner'),
    path('experienced/', views.ExperiencedDetailView.as_view(), name='experienced'),
    path('watching/', views.WatchingGamesDetailView.as_view(), name='watching'),
    path('other/sport/', views.OtherSportDetailView.as_view(), name='other_sport'),

    path('fortnite', views.FortniteDetailView.as_view(), name='fortnite'),
    path('pubg/', views.PubgDetailView.as_view(), name='pubg'),
    path('apex/', views.ApexDetailView.as_view(), name='apex'),
    path('minecraft/', views.MinecraftDetailView.as_view(), name='minecraft'),
    path('league/', views.LeagueDetailView.as_view(), name='league'),
    path('other/e_sport/', views.OtherESportDetailView.as_view(), name='other_e_sport'),

    path('read/book', views.ReadBookDetailView.as_view(), name='read_book'),
    path('social/gathering/', views.SocialGatheringDetailView.as_view(), name='social_gathering'),
    path('morning/', views.MorningActivityView.as_view(), name='morning'),
    path('other/hobby/', views.OtherHobbyDetailView.as_view(), name='other_hobby'),


]
