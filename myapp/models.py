import os
from django.db import models
from django.contrib import admin
from django.core.validators import FileExtensionValidator
from myapp.storage import OverwriteStorage

# Create your models here.
class DeviceModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def delete(self, *args, **kwargs):
        # Delete associated firmware files and branches
        for branch in self.firmwarebranch_set.all():
            branch.delete()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

class FirmwareBranch(models.Model):
    name = models.CharField(max_length=100)
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('device', 'name')  # Enforce uniqueness per DeviceModel

    def delete(self, *args, **kwargs):
        # Delete associated firmware files
        for firmware in self.firmware_set.all():
            if firmware.firmware_file:
                os.remove(firmware.firmware_file.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

def firmware_upload_path(instance, filename):
    return f'firmwares/{instance.device.name}-{instance.branch.id}-{instance.version}.bin'

class Firmware(models.Model):
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    version = models.CharField(max_length=10)
    firmware_file = models.FileField(upload_to=firmware_upload_path)
    branch = models.ForeignKey(FirmwareBranch, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('branch', 'version')  # Enforce uniqueness per Branch

    def delete(self, *args, **kwargs):
        # Delete the firmware file from the filesystem
        if self.firmware_file:
            os.remove(self.firmware_file.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.version
