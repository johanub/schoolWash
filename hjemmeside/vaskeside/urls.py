from django.urls import path
from .models import maskiner
from . import views

urlpatterns = [
    path('', views.frontpage, name='forside'),
    path('logind/', views.logind_view, name='logind'),
    path('reservertid/', views.reservertid, name='Reserver tid'),
    path('slettid/', views.slettid, name='Slet tid'),
]

for maskine in maskiner:
    alias = maskine[0].lower().replace(' ', '-')
    urlpatterns.append(path(alias +'/', views.nyvask, name=maskine[0]))
