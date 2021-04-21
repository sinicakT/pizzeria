from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Gallery


class GalleryAdmin(ModelAdmin):
    model = Gallery
    # menulabel = 'Pizza'
    menu_icon = 'pilcrow'
    menu_order = 100
    as_to_settings_menu = False
    exclude_from_explorer = False


modeladmin_register(GalleryAdmin)

