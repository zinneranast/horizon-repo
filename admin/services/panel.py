from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.admin import dashboard

class Services(horizon.Panel):
    name = _("Services")
    slug = "services"


dashboard.Admin.register(Services)
