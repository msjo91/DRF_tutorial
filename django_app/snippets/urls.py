from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import generics_cbv

urlpatterns = [
    url(r'^$', generics_cbv.SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', generics_cbv.SnippetDetail.as_view()),
    url(r'^(?P<pk>[0-9]+)/highlight/$', generics_cbv.SnippetHighlight.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
