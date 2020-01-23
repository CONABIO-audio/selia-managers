from django.db import models
from django.forms import ModelForm, widgets
from irekua_database.models import (
    Collection,
    PhysicalDevice,
    Site,
    User
)

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'
    def __init__ (self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.fields["physical_devices"].widget = widgets.CheckboxSelectMultiple()
        self.fields["physical_devices"].help_text = ""
        self.fields["physical_devices"].queryset = PhysicalDevice.objects.all()
        self.fields["sites"].widget = widgets.CheckboxSelectMultiple()
        self.fields["sites"].help_text = ""
        self.fields["sites"].queryset = Site.objects.all()
        self.fields["administrators"].widget = widgets.CheckboxSelectMultiple()
        self.fields["administrators"].help_text = ""
        self.fields["administrators"].queryset = User.objects.all()
        self.fields["users"].widget = widgets.CheckboxSelectMultiple()
        self.fields["users"].help_text = ""
        self.fields["users"].queryset = User.objects.all()