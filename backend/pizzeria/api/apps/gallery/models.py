from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel


class GalleryImage(Orderable):
    pizza = ParentalKey('gallery.Gallery', related_name='images', blank=True, default=None)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )

    panels = [
        ImageChooserPanel("image"),
    ]


class Gallery(ClusterableModel):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
        InlinePanel('images', label="Obrázky")
    ]

    class Meta:
        verbose_name = 'Galéria'
        verbose_name_plural = 'Galérie'
