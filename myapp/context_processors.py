def menu_items(request):
    menu_items = [
        {'name': 'Home', 'url': '/', 'icon': 'fa-solid fa-house'},
        {'name': 'Devices', 'url': '/devices/', 'icon': 'fa-solid fa-microchip'},
        # Add more menu items as needed
    ]
    return {'menu_items': menu_items}