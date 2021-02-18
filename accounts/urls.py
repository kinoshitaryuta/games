from django.urls import path
from.import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign_up/sub/', views.TemporaryRegistrationView.as_view(), name='sign_up_sub'),
    # path('sign_up/text/', views.TwoStageAuthenticationView.as_view(), name='sign_up_text'),
    # path('sign_up/main/<token>/', views.MainRegistrationView.as_view(), name='sign_up_main'),
    path('logout/', views.LogoutView.as_view(), name='logout'),


]