from django.conf.urls import url

from lookup.views import LookupSingle, NamespaceView

urlpatterns = [
    url(r'^id/(?P<identifier>.+)/$', LookupSingle.as_view(), name="id_single"),
    url(r'^namespace/(?P<namespace>.+)/$', NamespaceView.as_view(), name="lookup_namespace"),
]
