from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from openstack_dashboard.dashboards.admin.services import tables

import subprocess
import re

class ServiceTab(tabs.TableTab):
    table_classes = (tables.ServicesTable,)
    name = _("Services Tab")
    slug = "services_tab"
    template_name = "horizon/common/_detail_table.html"
    preload = False

#    def get_services_data(self):
#        services = []
##        try:
#            getServices = subprocess.Popen('./main.py service-list', shell=True, stdout=subprocess.PIPE)
#            services = getServices.stdout.readlines()
#            service_list = []
#            for i in services:
#                service_list.append(re.search('S1 ', i).group(0))
#            print re.search('S1 ', i).group(0) 
#        except Exception:
#            exceptions.handle(self.request,
#                              _('Unable to retrieve service information.'))

#        return service_list


class ServicesTabs(tabs.TableTab):
    slug = "services_tabs"
    tabs = (ServiceTab,)
    sticky = True
