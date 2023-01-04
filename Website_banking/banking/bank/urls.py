from.import views
from django.urls import path

from .views import HomeView, IndexView

app_name='bank'
urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('index', IndexView.as_view(), name='index'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('application', views.application, name='application'),


]