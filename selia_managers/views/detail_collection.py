from django.views.generic.detail import SingleObjectMixin
from django import forms

from irekua_database.models import Collection
from irekua_database.models import SamplingEvent
from irekua_database.models import CollectionSite
from irekua_database.models import CollectionDevice
from irekua_database.models import Item
from irekua_database.models import Annotation
from irekua_permissions.data_collections import users as user_permissions
from irekua_permissions import licences as licence_permissions

from selia_managers.views.detail_views.base import SeliaDetailView
from selia_managers.forms.json_field import JsonField


class CollectionUpdateForm(forms.ModelForm):
    metadata = JsonField()

    class Meta:
        model = Collection
        fields = [
            'metadata',
        ]


class DetailCollectionView(SeliaDetailView, SingleObjectMixin):
    model = Collection
    form_class = CollectionUpdateForm
    delete_redirect_url = 'selia_managers:collections'

    template_name = 'selia_managers/detail/manager_collection.html'

    help_template = 'selia_managers/help/manager_collection_detail.html'
    detail_template = 'selia_managers/details/manager_collection.html'
    summary_template = 'selia_managers/summaries/manager_collection.html'
    update_form_template = 'selia_managers/update/manager_collection.html'
    viewer_template = 'selia_managers/viewers/manager_collection.html'

    '''def has_view_permission(self):
        user = self.request.user
        return user_permissions.view(user, collection_user=self.object)

    def has_change_permission(self):
        user = self.request.user
        return user_permissions.change(user, collection_user=self.object)

    def has_delete_permission(self):
        user = self.request.user
        return user_permissions.delete(user, collection_user=self.object)
    
    def get_delete_redirect_url_args(self):
        return [self.object.name]

    def get_permissions(self):
        permissions = super().get_permissions()
        user = self.request.user
        permissions['list_collection_users'] = user_permissions.list(
            user, collection=self.object)
        permissions['list_collection_licences'] = licence_permissions.list(
            user, collection=self.object)
        return permissions

    def get_summary_info(self):
        user = self.request.user
        collection = self.object

        sampling_events = (
            SamplingEvent.objects
            .filter(collection=collection, created_by=user)
            .count())
        collection_sites = (
            CollectionSite.objects
            .filter(collection=collection, created_by=user)
            .count())
        collection_devices = (
            CollectionDevice.objects
            .filter(collection=collection, created_by=user)
            .count())
        items = (
            Item.objects
            .filter(
                sampling_event_device__sampling_event__collection=collection,
                created_by=user)
            .count())
        annotations = (
            Annotation.objects
            .filter(
                item__sampling_event_device__sampling_event__collection=collection,
                created_by=user)
            .count())

        return {
            'sampling_events': sampling_events,
            'collection_sites': collection_sites,
            'collection_devices': collection_devices,
            'items': items,
            'annotations': annotations,
        }
'''
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['collection'] = self.object
        # context['summary_info'] = self.get_summary_info()
        return context
