from django.urls import path,include
from.import views


urlpatterns=[
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('fortnite/', views.FortniteDetailView.as_view(), name='fortnite'),
    path('apex/', views.ApexDetailView.as_view(), name='apex'),
    path('Monhan/', views.MonhanDetailView.as_view(), name='Monhan'),
    path('Guraburu/', views.GuraburuDetailView.as_view(), name='Guraburu'),
    path('search_tweets/Guraburu/', views.search_tweets_guraburu, name='tweets_Guraburu'),
    path('search_tweets/Monhan/', views.search_tweets_monhan, name='tweets_Monhan'),

]
