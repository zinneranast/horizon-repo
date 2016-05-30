from horizon import exceptions, tables
from django.core.urlresolvers import reverse_lazy

from openstack_dashboard.dashboards.admin.services.tables import ServicesTable
from openstack_dashboard.dashboards.admin.services import forms as admin_forms
from openstack_dashboard.dashboards.admin.services import workflows as service_workflows

from horizon import workflows

import json

import subprocess
import re

class Service:
    def __init__(self, id, service_name, subnet_name, ip_address):
        self.id = id
        self.service_name = service_name
        #self.description = description
        self.ip_address = ip_address
        self.subnet_name  = subnet_name


class IndexView(tables.DataTableView):
    table_class = ServicesTable
    template_name = 'admin/services/index.html'

    def get_data(self):
        getServices = subprocess.Popen('./main.py service-list', shell=True, stdout=subprocess.PIPE)
        services = getServices.stdout.readlines()

        strobj = '['
        n = 1
        for i in services:
            if n is not 1:
                strobj = strobj + ','
            tmp = i.split()
            if  len(tmp) > 1:
                strobj = strobj + '{"id": %s, "service_name": "%s", "subnet_name": "%s", "ip_address": "%s"}' % (n, tmp[0], tmp[2], tmp[1])
            else:
                strobj = strobj + '{"id": %s, "service_name": "%s", "subnet_name": "-", "ip_address": "-"}' % (n, tmp[0])
            n += 1
        strobj = strobj + ']'
        print strobj

        instances = json.loads(strobj)
        services = []
        for i in instances:
            services.append(Service(i['id'], i['service_name'], i['subnet_name'], i['ip_address']))
        return services


#class GetView(forms.FormView):
#    form_class = admin_forms.GetService
#    template_name = 'admin/services/get.html'
#    success_url = reverse_lazy('horizon:admin:services:index')
#    submit_url = 'horizon:admin:services:get'

#    def get_initial(self):
##        service = self._get_object()
#        return {'id': service['id'],
#                'service_name': service['service_name']}#,
#                #'ip_address': service['ip_address'],
#                #'subnet_name': service['subnet_name']}


class GetView(workflows.WorkflowView):
    workflow_class = service_workflows.GetService
    template_name = 'admin/services/get.html'
#    page_title = _("Get Service")

    def get_initial(self):
        service_id = self.kwargs['id']

        try:
            # Get initial service information
            getServices = subprocess.Popen('./main.py service-list', shell=True, stdout=subprocess.PIPE)
            service_list = getServices.stdout.readlines()
            strobj = '['
            n = 1
            for i in service_list:
                tmp = i.split("\n")
                if n is not 1:
                    strobj = strobj + ','
                strobj = strobj + '{"id": %s, "service_name": "%s"}' % (n, tmp[0])
                n += 1
            strobj = strobj + ']'

            instances = json.loads(strobj)
            services = []
            for i in instances:
                services.append(Service(i['id'], i['service_name'])) #, i['ip_addre$

        except Exception:
            exceptions.handle(self.request,
                              _('Unable to retrieve service details.'),
                              redirect=reverse_lazy(INDEX_URL))
        return {'service_id': services.id,
                'service_name': services.service_name}
