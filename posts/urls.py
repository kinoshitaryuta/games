from django.urls import path
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

]
