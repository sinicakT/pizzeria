from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import Size, Unit


class SizeAdmin(ModelAdmin):
    model = Size
    menulabel = 'Veľkosti'
    # menu_icon = 'pilcrow'
    menu_order = 100
    add_to_settings_menu = True
    exclude_from_explorer = True
    list_display = ('name', )
    # list_filter = ('name', )
    search_fields = ('name', )


class UnitAdmin(ModelAdmin):
    model = Unit
    menu_label = 'Jednotky'
    # menu_icon = 'edit'
    menu_order = 100
    add_to_settings_menu = True
    exclude_from_explorer = True
    list_display = ('name', )
    # list_filter = ('name', )
    search_fields = ('name', )


modeladmin_register(SizeAdmin)
modeladmin_register(UnitAdmin)
