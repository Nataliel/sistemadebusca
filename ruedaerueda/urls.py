from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.core.views import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView, LogListView
from ruedaerueda import settings


handler404 = 'apps.core.views.page_not_found'
handler500 = 'apps.core.views.page_not_found'

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^admin/', include(admin.site.urls)),
    (r'^selectable/', include('selectable.urls')),
    url(r'^$', BaseListView.as_view(), name='home'),
    url(r'^logs/$', LogListView.as_view(), name='logs'),
    url(r'^criar/$', BaseCreateView.as_view(), name='criar'),
    url(r'^editar/(?P<pk>\d+)/$', BaseUpdateView.as_view(), name='editar'),
    url(r'^excluir/(?P<pk>\d+)/$', BaseDeleteView.as_view(), name='excluir'),
)
