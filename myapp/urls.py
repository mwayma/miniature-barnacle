from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/<int:device_id>/', views.device_detail, name='device_detail'),
    path('devices/<int:device_id>/create-branch/', views.create_branch, name='create_branch'),
    path('devices/create/', views.create_device, name='create_device'),
    path('upload-firmware/', views.upload_firmware, name='upload_firmware'),
    path('upload-firmware/<int:firmware_id>/', views.upload_firmware, name='edit_firmware'),
    path('delete-firmware/<int:firmware_id>/', views.delete_firmware, name='delete_firmware'),
    path('delete-device/<int:device_id>/', views.delete_device, name='delete_device'),
    path('delete-branch/<int:branch_id>/', views.delete_branch, name='delete_branch'),
    
]
