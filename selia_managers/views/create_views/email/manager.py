from selia_managers.views.create_views.manager_base import CreateManagerBase


class CreateEmailManager(CreateManagerBase):
    manager_name = 'selia_managers:create_email'

    def view_from_request(self):
        if 'collection' not in self.request.GET:
            return 'selia_managers:create_email_select_collection'
        if 'user' not in self.request.GET:
            return 'selia_managers:create_email_select_user'

        return 'selia_managers:create_email_create_form'
