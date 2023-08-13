from django import forms
from django.core.validators import FileExtensionValidator
from .models import Firmware, DeviceModel, FirmwareBranch

class FirmwareUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs and 'device' in kwargs['initial']:
            self.fields['branch'].queryset = FirmwareBranch.objects.filter(device=kwargs['initial']['device'])

    class Meta:
        model = Firmware
        fields = '__all__'

class FirmwareEditForm(forms.ModelForm):
    class Meta:
        model = Firmware
        fields = ['version', 'firmware_file', 'branch']

class DeviceModelForm(forms.ModelForm):
    class Meta:
        model = DeviceModel
        fields = '__all__'
