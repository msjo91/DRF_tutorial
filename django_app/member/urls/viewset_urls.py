from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.viewsets_cbv import UserViewSet

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', user_list, name='user-list'),
    url(r'^(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])
