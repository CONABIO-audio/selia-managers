from selia_managers.views.create_views.manager_base import CreateManagerBase


class CreateAdministratorManager(CreateManagerBase):
    manager_name = 'selia_managers:create_administrator'

    def view_from_request(self):
        if 'collection' not in self.request.GET:
            return 'selia_managers:delete_administrator_select_collection'
        if 'user' not in self.request.GET:
            return 'selia_managers:delete_administrator_select_user'

        return 'selia_managers:delete_administrator_delete_form'
