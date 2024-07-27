from django import template
from tree_menu.models import Menu, MenuItem


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {
            'menu_items': [],
            'expanded_items': [],
            'active_item': None,
            'request': request
        }

    menu_items = MenuItem.objects.filter(menu=menu).select_related(
        'parent'
    ).prefetch_related('children')

    active_item = None
    for item in menu_items:
        item_url = item.get_absolute_url()
        if item_url == request.path:
            active_item = item
            break

    expanded_items = set()
    if active_item:
        parent = active_item.parent
        while parent:
            expanded_items.add(parent)
            parent = parent.parent
        expanded_items.add(active_item)

    return {
        'menu_items': menu_items,
        'expanded_items': expanded_items,
        'active_item': active_item,
        'request': request,
    }
