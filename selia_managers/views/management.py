from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from irekua_database.models import CollectionType, Collection


@login_required
def management(request):
    user = request.user
 
    queryset = CollectionType.objects.all()
    collectiontype_admin_query = Q(administrators=user)
    queryset = queryset.filter(collectiontype_admin_query).distinct()

    if not queryset:
        return render(
          request,
          'selia_templates/generic/no_permission.html'
        )

    context = {
      'user': user,
      'collection_type': queryset
    }

    return render(request, 'selia_managers/management.html', context)
