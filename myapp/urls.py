from django.urls import path
from myapp.views import homepage  # Replace 'myapp' with the name of your app

urlpatterns = [
    path('', homepage, name='homepage'),
    # Add other URL patterns for your app's views here
]
