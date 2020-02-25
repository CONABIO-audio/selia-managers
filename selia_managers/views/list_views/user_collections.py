from django.db.models import Q
from irekua_database.models import Collection

from selia_managers.views.list_views.base import SeliaListView
from irekua_filters.data_collections import data_collections


class ListUserCollectionsView(SeliaListView):
    template_name = 'selia_managers/list/user_collections.html'

    list_item_template = 'selia_managers/list_items/collection.html'
    help_template = 'selia_managers/help/user_collections.html'
    filter_form_template = 'selia_managers/filters/collection.html'

    filter_class = data_collections.Filter
    search_fields = data_collections.search_fields
    ordering_fields = data_collections.ordering_fields

    def get_initial_queryset(self):
        user = self.request.user

        queryset = Collection.objects.all()

        if user.is_special:
            return queryset

        collection_user_query = Q(collectionuser__user=user)
        collection_admin_query = Q(administrators=user)
        collection_type_admin = Q(collection_type__administrators=user)

        queryset = queryset.filter(
            collection_user_query |
            collection_admin_query |
            collection_type_admin).distinct()

        return queryset

    def has_view_permission(self):
        return self.request.user.is_authenticated
