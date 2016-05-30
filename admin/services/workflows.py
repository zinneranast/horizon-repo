from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import workflows

from openstack_dashboard import api


class GetService(workflows.Workflow):
    slug = "get_service"
    name = _("Get Service")
    finalize_button_name = _("Save")
    success_message = _('Service is connected "%s".')
    failure_message = _('Unable to connct service "%s" to subnet.')
    success_url = "horizon:admin:services:index"
#    default_steps = (UpdateFlavorInfo,
#                     UpdateFlavorAccess)

    def format_status_message(self, message):
        return message % self.context['service_name']

#    def handle(self, request, data):
#        service_projects = data["flavor_access"]
#        is_public = not flavor_projects

        # Update flavor information
#        try:
#            service_id = data['service_id']
            # Grab any existing extra specs, because flavor edit is currently
            # implemented as a delete followed by a create.
#            extras_dict = api.nova.flavor_get_extras(self.request,
#                                                     flavor_id,
#                                                     raw=True)
            # Mark the existing flavor as deleted.
#            api.nova.flavor_delete(request, flavor_id)
            # Then create a new flavor with the same name but a new ID.
            # This is in the same try/except block as the delete call
            # because if the delete fails the API will error out because
            # active flavors can't have the same name.
#            flavor = api.nova.flavor_create(request,
#                                            data['name'],
#                                            data['memory_mb'],
#                                            data['vcpus'],
#                                            data['disk_gb'],
#                                            ephemeral=data['eph_gb'],
#                                            swap=data['swap_mb'],
#                                            is_public=is_public)
#            if (extras_dict):
#                api.nova.flavor_extra_set(request, flavor.id, extras_dict)
#        except Exception:
#            exceptions.handle(request, ignore=True)
#            return False

        # Add flavor access if the flavor is not public.
#        for project in flavor_projects:
##            try:
#                api.nova.add_tenant_to_flavor(request, flavor.id, project)
#            except Exception:
#                exceptions.handle(request, _('Modified flavor information, '
#                                             'but unable to modify flavor '
#                                             'access.'))
#        return True
