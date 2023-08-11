from django.shortcuts import render

# Create your views here.
def homepage(request):
    menu_items = [
        {'name': 'Home', 'url': '/', 'icon': 'fa-solid fa-house',},  # Replace '/' with the appropriate URL for the home page
        {'name': 'About', 'url': '/about/', 'icon': 'fa-solid fa-poo'},
        # Add more menu items as needed
    ]
    context = {'menu_items': menu_items}
    return render(request, 'myapp/index.html', context)