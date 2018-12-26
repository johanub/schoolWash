from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.logind_view, name='logind'),
]
#todo get clean.png on site

