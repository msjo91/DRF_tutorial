from django.conf.urls import url

from .views import generics_cbv

urlpattern = [
    url(r'^$', generics_cbv.UserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', generics_cbv.UserDetail.as_view()),
]
