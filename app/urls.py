from django.urls import path
from.import views


urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('help/',views.HelpView.as_view(),name='help'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
    path('my_page/<int:pk>/', views.MyPageView.as_view(), name='my_page'),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('terms/', views.TermsOfServiceView.as_view(), name='terms'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),

]
