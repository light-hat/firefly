from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from os import environ

# Страницы на сайте.
urlpatterns = [
    #path('', login_required(views.ArchiveView.as_view()), name="archive"),
]

# Вспомогательные страницы веб-приложения.
urlpatterns += [
    #path('login/', views.LoginPageView.as_view()),
    path('logout/', LogoutView.as_view()),
]
