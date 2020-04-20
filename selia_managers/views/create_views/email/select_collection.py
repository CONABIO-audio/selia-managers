# from irekua_filters.data_collections import data_collections
from irekua_database.models import CollectionType
from selia_managers.views.utils import SeliaList
from selia_managers.views.create_views import SeliaSelectView

from django.utils.translation import gettext as _
from django_filters import FilterSet
from irekua_database.models import Collection


class Filter(FilterSet):
    class Meta:
        model = Collection
        fields = {
            'name': ['icontains'],
            'created_on': ['gt', 'lt']
        }


search_fields = (
    'name',
    'description'
)

ordering_fields = (
    ('created_on', _('created on')),
    ('name', _('name')),
)


class SelectCollectionEmailView(SeliaSelectView):
    template_name = 'selia_managers/create/email/select_collection.html'
    prefix = 'collection'
    create_url = 'selia_managers:create_email'

    def get_list_class(self):
        class CollectionList(SeliaList):
            filter_class = Filter
            search_fields = search_fields
            ordering_fields = ordering_fields
            queryset = Collection.objects.filter(collection_type__in=self.request.user.collectiontype_set.all())
            # queryset = self.request.user.managed_collection

            list_item_template = 'selia_managers/select_list_items/collection.html'
            filter_form_template = 'selia_managers/filters/collection.html'

        return CollectionList
