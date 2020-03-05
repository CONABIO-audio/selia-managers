from django.shortcuts import render
from .forms import CollectionForm
from irekua_database.models import User, CollectionType

from django.db.models import Q
from irekua_database.models import Collection

from selia_managers.views.list_views.base import SeliaListView
from irekua_filters.data_collections import data_collections


def collections(request):
  current_user = request.user

  context = {
    'dummy_text': 'BLA BLA BLA',
    'collection_form': CollectionForm()
  }

  return render(request, 'selia_managers/collections.html', context)



class listManagerCollectionsView(SeliaListView):
  template_name = 'selia_managers/list/user_collections.html'

  list_item_template = 'selia_managers/list_items/collection.html'
  help_template = 'selia_managers/help/user_collections.html'
  filter_form_template = 'selia_managers/filters/collection.html'

  filter_class = data_collections.Filter
  search_fields = data_collections.search_fields
  ordering_fields = data_collections.ordering_fields

  print('****CollectionType****')
  collection_types = CollectionType.objects.all()
  for c in collection_types:
    print(c)


  def get_initial_queryset(self):
    user = self.request.user
    # print(user)
    print('****USER****')
    # user = User.objects.first()
    print(user)
    queryset = user.managed_collections #Collection.objects.all()

    if user.is_special:
      return queryset

    #collection_user_query = Q(collectionuser__user=user)
    #collection_admin_query = Q(administrators=user)
    #collection_type_admin = Q(collection_type__administrators=user)

    #queryset = queryset.filter(
    #  collection_user_query |
    #  collection_admin_query |
    #  collection_type_admin).distinct()

    return queryset

  def has_view_permission(self):
    return self.request.user.is_authenticated