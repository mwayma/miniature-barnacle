from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/<int:device_id>/', views.device_detail, name='device_detail'),
    path('devices/<int:device_id>/create-branch/', views.create_branch, name='create_branch'),
    path('devices/create/', views.create_device, name='create_device'),
    path('upload-firmware/<int:device_id>/', views.upload_firmware, name='upload_firmware'),
    path('edit-firmware/<int:firmware_id>/', views.edit_firmware, name='edit_firmware'),
    path('delete-firmware/<int:firmware_id>/', views.delete_firmware, name='delete_firmware'),
    path('delete-device/<int:device_id>/', views.delete_device, name='delete_device'),
    path('delete-branch/<int:branch_id>/', views.delete_branch, name='delete_branch'),
    path('<str:device_name>/<int:branch_id>/', views.firmware_info, name='firmware_info'),    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)