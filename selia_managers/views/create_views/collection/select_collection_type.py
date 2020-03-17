# from irekua_filters.data_collections import data_collections
from irekua_database.models import CollectionType
from selia_managers.views.utils import SeliaList
from selia_managers.views.create_views import SeliaSelectView

from django.utils.translation import gettext as _
from django_filters import FilterSet
from irekua_database.models import CollectionType


class Filter(FilterSet):
    class Meta:
        model = CollectionType
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


class SelectCollectionCollectionView(SeliaSelectView):
    template_name = 'selia_managers/create/collection/select_collection_type.html'
    prefix = 'collection_type'
    create_url = 'selia_managers:create_collection'

    def get_list_class(self):
        class CollectionList(SeliaList):
            filter_class = Filter
            search_fields = search_fields
            ordering_fields = ordering_fields
            queryset = CollectionType.objects.all()
            queryset = queryset.filter(administrators=self.request.user).distinct()

            list_item_template = 'selia_managers/select_list_items/collection_type.html'
            filter_form_template = 'selia_managers/filters/collection_type.html'

        return CollectionList
