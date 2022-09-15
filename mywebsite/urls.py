from django.urls import re_path, include
from django.contrib import admin
from. import views
urlpatterns = [
	re_path(r'^blog/', include('blog.urls',namespace = 'blog')),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^admin/', admin.site.urls),
]
