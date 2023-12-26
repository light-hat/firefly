#from api.v1 import views
from rest_framework import routers
from django.urls import include, path
from django.contrib.auth.decorators import login_required


router = routers.DefaultRouter()

#router.register(r'profile', views.ProfileViewSet)

# Описание возможных url-адресов на сайте.
urlpatterns = [
    path('', include(router.urls)),

    #path('object/settings/', login_required(views.SettingsControlView.as_view({'post': 'create'}))),
]
