from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.social, name='social'),
    path('upload/', views.upload, name='upload'),
]

