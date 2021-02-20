from django.urls import path
from.import views


urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('help/',views.HelpView.as_view(),name='help'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
]
