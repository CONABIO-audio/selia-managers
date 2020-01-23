from django.shortcuts import render
from .forms import CollectionForm


def collections(request):
  context = {
    'collection_form': CollectionForm()
  }

  return render(request, 'selia_managers/collections.html', context)
