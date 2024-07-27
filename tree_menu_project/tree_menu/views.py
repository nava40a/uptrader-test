from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Menu


def index(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus
    }
    return render(request, 'index.html', context)



def dynamic_view(request, path):
    menu_item = get_object_or_404(
        MenuItem.objects.select_related(
            'menu'
        ).prefetch_related('children__children'), url=f'/{path}/')
    return render(request, 'page.html', {'menu_item': menu_item})
