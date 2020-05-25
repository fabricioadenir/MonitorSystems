from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('login', views.login, name='login'),
    path('user', views.user, name='user'),
    path('favicon.png', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.png')))
]