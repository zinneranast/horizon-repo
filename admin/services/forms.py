from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import messages

from openstack_dashboard import api


class GetService(forms.SelfHandlingForm):
    subnet_name = forms.CharField(label=_("Subnet Name"),
                           required=False)
    failure_url = 'horizon:admin:services:index'

    def handle(self, request, data):
        try:
            params = {'service_name': data['service_name'],
                      'subnet_name': data['subnet_name']}
            msg = _('Service %s was successfully connected to subnet %s.') % (data['service_name'], data['subnet_name'])
            messages.success(request, msg)
        except Exception:
            msg = _('Failed to connect service %s to subnet %s.') % (data['service_name'], data['subnet_name'])
            redirect = reverse(self.failure_url)
            exceptions.handle(request, msg, redirect=redirect)
