from django.conf.urls import include, url
from . import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', index.index, name = 'index'),
    url(r'^decomposed/$', index.result, name = 'decomposed'),
] + staticfiles_urlpatterns()
