import os

from django.shortcuts import render, redirect, get_object_or_404
from .forms import FirmwareUploadForm, DeviceModelForm
from .models import Firmware, DeviceModel, FirmwareBranch
from django.urls import reverse
from django.conf import settings

# Create your views here.
def homepage(request):
    return render(request, 'myapp/index.html')

def device_list(request):
    devices = DeviceModel.objects.all()
    return render(request, 'myapp/devices.html', {'devices': devices})

def create_device(request):
    if request.method == 'POST':
        form = DeviceModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceModelForm()
    return render(request, 'myapp/device_form.html', {'form': form})

def device_detail(request, device_id):
    device = get_object_or_404(DeviceModel, pk=device_id)
    firmware_by_branch = {}

    firmware = Firmware.objects.filter(device=device).order_by('branch', 'version')
    for fw in firmware:
        if fw.branch not in firmware_by_branch:
            firmware_by_branch[fw.branch] = []
        firmware_by_branch[fw.branch].append(fw)

    context = {
        'device': device,
        'firmware_by_branch': firmware_by_branch,
        'form': DeviceModelForm(instance=device),
    }

    return render(request, 'myapp/device_detail.html', context)



def edit_device(request, device_id):
    device = get_object_or_404(DeviceModel, pk=device_id)

    # Get the distinct branches for the firmwares of this device model
    firmware_branches = Firmware.objects.filter(device=device).values_list('branch', flat=True).distinct()

    # Create a dictionary to store firmware data for each branch
    firmware_data = {}
    for branch in firmware_branches:
        firmwares = Firmware.objects.filter(device=device, branch=branch).order_by('version')
        firmware_data[branch] = firmwares

    # Create a form for uploading firmware
    firmware_upload_form = FirmwareUploadForm()

    context = {
        'device': device,
        'firmware_data': firmware_data,
        'firmware_upload_form': firmware_upload_form,
    }

    return render(request, 'myapp/edit_device.html', context)


def delete_device(request, device_id):
    device = get_object_or_404(DeviceModel, pk=device_id)
    if request.method == 'POST':      
        device.delete()
        return redirect('device_list')  # Redirect to the firmware list page after deletion
    return redirect('edit_device', device_id=device_id)  # Redirect back to the edit page if not a POST request

def create_branch(request, device_id):
    device = get_object_or_404(DeviceModel, pk=device_id)

    if request.method == 'POST':
        branch_name = request.POST.get('branch_name')
        if branch_name:
            FirmwareBranch.objects.create(name=branch_name, device=device)  # Corrected this line
        return redirect('device_detail', device_id=device_id)

    return render(request, 'myapp/create_branch.html', {'device': device})

def delete_branch(request, branch_id):
    branch = get_object_or_404(FirmwareBranch, pk=branch_id)
    if request.method == 'POST':
        branch.delete()
        return redirect('device_detail', device_id=branch.device.id)
    return redirect('device_detail', device_id=branch.device.id)  # Redirect back to the device details page if not a POST request

def firmware(request):
    firmware_items = Firmware.objects.all()
    context = {'firmware_items': firmware_items}
    return render(request, 'myapp/firmware.html', context)

def upload_firmware(request, firmware_id=None):
    is_editing = firmware_id is not None

    if is_editing:
        firmware = get_object_or_404(Firmware, pk=firmware_id)
        form = FirmwareUploadForm(request.POST or None, request.FILES or None, instance=firmware)
    else:
        form = FirmwareUploadForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            firmware = form.save()  # Let Django handle the file overwrite
            device_id = firmware.device_id
            redirect_url = reverse('device_detail', kwargs={'device_id': device_id})
            return redirect(redirect_url)

    context = {'form': form, 'is_editing': is_editing}

    return render(request, 'myapp/upload_firmware.html', context)

def delete_firmware(request, firmware_id):
    firmware = get_object_or_404(Firmware, pk=firmware_id)
    if request.method == 'POST':
        device_id = firmware.device_id
        firmware.delete()
        redirect_url = reverse('device_detail', kwargs={'device_id': device_id})
        return redirect(redirect_url)
    return redirect('upload_firmware', firmware_id=firmware_id)  # Redirect back to the edit page if not a POST request