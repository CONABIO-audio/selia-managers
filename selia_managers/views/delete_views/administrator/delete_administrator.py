from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from selia_managers.views.create_views.create_base import SeliaCreateView
from irekua_database.models import User
from irekua_database.models import Collection

from selia_managers.forms.json_field import JsonField


def SaveAdministrator(request):
    collection = Collection.objects.get(name=request.GET['collection'])
    user = User.objects.get(pk=request.GET['user'])

    collection.remove_administrator(user)

    return redirect('../../../collections')


def CreateAdministratorView(request):
    template_name = 'selia_managers/delete/administrator/delete_form.html'
    success_url = 'selia_managers:management'

    collection = Collection.objects.get(name=request.GET['collection'])
    user = User.objects.get(pk=request.GET['user'])

    context = {
      'user': user,
      'collection': collection
    }

    return render(request, template_name, context)
