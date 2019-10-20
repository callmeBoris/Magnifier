from django.urls import path
from . import views

app_name = 'magnifier'
urlpatterns = [
    path('', views.home, name='home'),
    path('results', views.results, name='results')
]