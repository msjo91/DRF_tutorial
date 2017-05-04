from django.conf.urls import url
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.viewsets_cbv import SnippetViewSet

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = format_suffix_patterns([
    url(r'^$', snippet_list, name='snippet-list'),
    url(r'^(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
])
