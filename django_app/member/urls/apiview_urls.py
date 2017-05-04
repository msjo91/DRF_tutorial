from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import generics_cbv

urlpatterns = [
    url(r'^$', generics_cbv.UserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', generics_cbv.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
