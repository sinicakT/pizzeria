from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Pizza, Offer, Ingredient, Allergen


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


class OfferAdmin(ModelAdmin):
    model = Offer
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


modeladmin_register(PizzaAdmin)
modeladmin_register(OfferAdmin)
modeladmin_register(IngredientAdmin)
modeladmin_register(AllergenAdmin)
