from django.urls import re_path

from . import views
app_name='blog'
urlpatterns = [
	re_path(r'^create/$', views.create, name='create'),
	re_path(r'^$', views.index, name='index'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
