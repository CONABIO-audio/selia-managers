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
        '''self.user = User.objects.get(
            pk=self.request.GET['user'])
        self.role = Role.objects.get(
            pk=self.request.GET['role'])
        '''
        return {
            'collection_type': self.collection_type,
            # 'role': self.role,
            # 'user': self.user,
        }

    def get_success_url_args(self):
        return [self.request.GET['collection_type']]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['collection_type'] = self.collection_type
        # context['selected_user'] = self.user
        # context['role'] = self.role

        '''role_info = CollectionRole.objects.get(
            collection_type=self.collection.collection_type,
            role=self.role)
        context['role_info'] = role_info
        
        context['form'].fields['metadata'].update_schema(
            role_info.metadata_schema)
        '''
        return context
