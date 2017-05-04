"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from member.views import viewsets_cbv as member_view
from snippets.views import viewsets_cbv as snippets_view

router = routers.DefaultRouter()
router.register(r'member', member_view.UserViewSet)
router.register(r'snippets', snippets_view.SnippetViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^member/', include('member.urls.viewset_urls')),
    # url(r'^snippets/', include('snippets.urls.viewset_urls')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# urlpatterns += format_suffix_patterns([url(r'^', fbv.api_root)])
