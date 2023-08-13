from django import forms
from django.core.validators import FileExtensionValidator
from .models import Firmware, DeviceModel

class FirmwareUploadForm(forms.ModelForm):
    class Meta:
        model = Firmware
        fields = '__all__'

class DeviceModelForm(forms.ModelForm):
    class Meta:
        model = DeviceModel
        fields = '__all__'
