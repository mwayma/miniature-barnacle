from django.test import TestCase
from .models import DeviceModel, FirmwareBranch, Firmware

class DeviceModelDeletionTestCase(TestCase):
    def setUp(self):
        # Create a DeviceModel instance with associated FirmwareBranch and Firmware
        self.device = DeviceModel.objects.create(name='Test Device', description='Test Description')
        self.branch = FirmwareBranch.objects.create(name='Test Branch', device=self.device)
        self.firmware = Firmware.objects.create(device=self.device, version='1.0', branch=self.branch)

    def test_device_deletion_cascades(self):
        # Delete the DeviceModel instance
        self.device.delete()

        # Check if associated objects are deleted
        self.assertFalse(DeviceModel.objects.filter(id=self.device.id).exists())
        self.assertFalse(FirmwareBranch.objects.filter(id=self.branch.id).exists())
        self.assertFalse(Firmware.objects.filter(id=self.firmware.id).exists())

    def test_firmware_files_deleted(self):
        # Get the firmware file path before deletion
        firmware_file_path = self.firmware.firmware_file.path

        # Delete the DeviceModel instance
        self.device.delete()

        # Check if firmware file is deleted from the filesystem
        self.assertFalse(os.path.exists(firmware_file_path))
