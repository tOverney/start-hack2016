from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import index

urlpatterns = [
    url(r'^$', index.index, name = 'index'),
    url(r'^decomposed/$', index.result, name = 'decomposed'),
    url(r'^concepts/$', index.concept_info, name = 'concept_info'),
    url(r'^contact/$', index.contact, name = 'contact'),
    url(r'^about/$', index.contact, name = 'about'),
    url(r'^audio/', index.audio, name = 'audio'),
] + staticfiles_urlpatterns()