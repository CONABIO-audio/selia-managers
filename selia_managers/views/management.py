from django.shortcuts import render
from irekua_database.models import CollectionType
from django.db.models import Q

def management(request):
  user = request.user
  queryset = CollectionType.objects.all()


  collectiontype_admin_query = Q(administrators=user)

  queryset = queryset.filter(collectiontype_admin_query).distinct()

  for q in queryset:
    print(q)
  
  context = {
    'user': user,
    'collection_type': queryset
  }

  return render(request, 'selia_managers/management.html', context)
