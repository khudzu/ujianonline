from django.urls import re_path

from . import views
app_name='blog'
urlpatterns = [
	re_path(r'^create/$', views.create, name='create'),
	re_path(r'^$', views.index, name='index'),
]