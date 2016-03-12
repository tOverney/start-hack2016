from django.conf.urls import include, url
from . import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', index.index, name = 'index'),
    url(r'^decomposed/$', index.result, name = 'decomposed'),
    url(r'^concepts/$', index.concept_info, name = 'concept_info'),
    url(r'^contact/$', index.contact, name = 'contact'),
    url(r'^about/$', index.contact, name = 'about'),
] + staticfiles_urlpatterns()