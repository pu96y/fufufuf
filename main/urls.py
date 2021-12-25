from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.glav, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.index, name='blog')
]
