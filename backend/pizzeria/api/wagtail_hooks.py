from wagtail.core import hooks

@hooks.register('construct_main_menu')
def hide_menu_items(request, menu_items):
    hide_items = ['reports', 'documents', 'explorer', 'reports']
    menu_items[:] = [item for item in menu_items if item.name not in hide_items]


@hooks.register('construct_settings_menu')
def hide_user_menu_item(request, menu_items):
    hide_items = ['presmerovania', 'stranky', 'kolekcie', 'workflows', 'workflow-tasks']
    menu_items[:] = [item for item in menu_items if item.name not in hide_items]

