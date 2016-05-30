from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.admin.services import views


SERVICES = r'^(?P<id>[^/]+)/%s$'

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(SERVICES % 'get', views.GetView.as_view(), name='get')
)
