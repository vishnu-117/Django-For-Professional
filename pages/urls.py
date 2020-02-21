from django.urls import path
from django.contrib.auth import views
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(), name='about'),
    # path('login/', views.LoginView.as_view(), name='login'),
]
