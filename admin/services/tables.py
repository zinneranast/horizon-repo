from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard import policy


class ServicesFilterAction(tables.FilterAction):
    name = "services_filter"


class GetService(policy.PolicyTargetMixin, tables.LinkAction):
    name = "get"
    verbose_name = _("Connect Service")
    url = "horizon:admin:services:get"
    classes = ("ajax-modal",)
    icon = "pencil"
    policy_rules = (("service", "get_service"),)


class ServicesTable(tables.DataTable):
    service_name = tables.Column("service_name", verbose_name=_("Service"))
    description = tables.Column("description", verbose_name=_("Description"))
    subnet_name = tables.Column("subnet_name", verbose_name=_("Subnet"))
    ip_address = tables.Column("ip_address", verbose_name=_("IP"))

    class Meta:
        name = "services"
        verbose_name = _("Services")
        table_actions = (ServicesFilterAction,)
        row_actions = (GetService,)
