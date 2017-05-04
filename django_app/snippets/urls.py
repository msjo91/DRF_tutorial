from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import cbv

urlpatterns = [
    url(r'^$', cbv.SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', cbv.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
