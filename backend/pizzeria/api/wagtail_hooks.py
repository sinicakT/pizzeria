from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Pizza, Size, Allergen, Ingredient, Unit, Menu


class PizzaAdmin(ModelAdmin):
    model = Pizza
    # menulabel = 'Pizza'
    menu_icon = 'pilcrow'
    menu_order = 100
    as_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('number', 'name')
    list_filter = ('number', )
    search_fields = ('number', 'name')


class MenuAdmin(ModelAdmin):
    model = Menu
    menulabel = 'Ostatná ponuka'
    menu_icon = 'pilcrow'
    menu_order = 100
    as_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', )
    search_fields = ('name', )


class IngredientAdmin(ModelAdmin):
    model = Ingredient
    menu_label = 'Prílohy'
    menu_icon = 'edit'
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', )
    list_filter = ('allergens', )
    search_fields = ('name', )


class AllergenAdmin(ModelAdmin):
    model = Allergen
    menu_label = 'Alergény'
    # menu_icon = 'edit'
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('number', 'name')
    # list_filter = ('name', )
    search_fields = ('name', )


class SizeAdmin(ModelAdmin):
    model = Size
    menulabel = 'Veľkosti'
    # menu_icon = 'pilcrow'
    menu_order = 100
    as_to_settings_menu = True
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


modeladmin_register(PizzaAdmin)
modeladmin_register(MenuAdmin)
modeladmin_register(SizeAdmin)
modeladmin_register(IngredientAdmin)
modeladmin_register(AllergenAdmin)
modeladmin_register(UnitAdmin)
