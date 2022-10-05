from django.urls import path
from .views import *
from . import views

urlpatterns = [
#path('', views.test, name="test"),
path('', homeView.as_view(), name='homeView'),
path('imgdetail/<int:pk>', detailView.as_view(), name='detailView'),
path('upload/', uploadView.as_view(), name='uploadView'),
path('searchResult', views.searchResult, name='searchResult')
]