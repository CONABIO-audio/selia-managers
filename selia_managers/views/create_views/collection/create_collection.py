from django import forms

from selia_managers.views.create_views.create_base import SeliaCreateView
from irekua_database.models import CollectionType
from irekua_database.models import Collection

from selia_managers.forms.json_field import JsonField


class CreateCollectionForm(forms.ModelForm):
    metadata = JsonField()

    class Meta:
        model = Collection
        fields = [
            'collection_type',
            'name',
            'description',
            'metadata',
            'logo',
            'is_open'
        ]


class CreateCollectionView(SeliaCreateView):
    template_name = 'selia_managers/create/collection/create_form.html'
    success_url = 'selia_managers:collections'

    model = Collection
    form_class = CreateCollectionForm

    def get_initial(self, *args, **kwargs):
        self.collection_type = CollectionType.objects.get(
            name=self.request.GET['collection_type'])

        return {
            'collection_type': self.collection_type
        }

    def get_success_url_args(self):
        return [self.request.GET['collection_type']]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['collection_type'] = self.collection_type

        return context

    def get_form(self, **kwargs):
        collection_type = CollectionType.objects.get(name=self.request.GET['collection_type'])
        form = super().get_form(**kwargs)
        schema = collection_type.metadata_schema
        form.fields['metadata'].update_schema(schema)
        return form