from django import template

from app_menu.models import Menu

register = template.Library()
template_name = 'app_menu/main_menu.html'


@register.inclusion_tag(filename=template_name, takes_context=True)
def draw_menu(context, menu_name, url_name):
    menu = Menu.objects.filter(name=menu_name).prefetch_related('items').first()
    menu_all_items = menu.items.order_by('title')

    menu_dict = {}

    menu_primary_items = [item for item in menu_all_items.filter(parent=None)]

    if url_name:
        menu_list = []

        current_item = menu_all_items.get(url_name=url_name)

        current_branch_ids = get_current_branch_ids_list(current_item, menu_primary_items, current_item.id)

        for item in menu_primary_items:
            item_dict = {'item': item, 'childs': []}

            if item.id in current_branch_ids:
                item_dict['childs'] = get_branch(item.id, item.childs.all(), current_branch_ids)

            menu_list.append(item_dict)

    else:
        menu_list = [{'item': item, 'childs': []} for item in menu_primary_items]

    menu_dict['items'] = menu_list

    return menu_dict


def get_current_branch_ids_list(parent, primary_m_items, selected_item_id):
    current_branch_ids_list = []

    while parent:
        current_branch_ids_list.append(parent.id)
        parent = parent.parent

    if not current_branch_ids_list:
        for item in primary_m_items:
            if item.id == selected_item_id:
                current_branch_ids_list.append(selected_item_id)

    return current_branch_ids_list


def get_branch(current_item_id, items, branch_ids):
    lst = []

    for item in items:
        childs = item.childs.all()

        item_dict = {'item': item, 'childs': []}

        if item.id in branch_ids:
            item_dict['childs'] = get_branch(current_item_id, childs, branch_ids)

        lst.append(item_dict)

    return lst
