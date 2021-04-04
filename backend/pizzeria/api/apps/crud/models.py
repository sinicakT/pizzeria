from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel


class Size(models.Model):

    class Meta:
        verbose_name = 'Veľkosť'
        verbose_name_plural = 'Veľkosti'

    name = models.CharField(verbose_name='Názov', max_length=30, default=None)

    def __str__(self):
        return str(self.name)


class Unit(models.Model):

    class Meta:
        verbose_name = 'Jednotka'
        verbose_name_plural = 'Jednotky'

    def __str__(self):
        return self.unit_code

    name = models.CharField(verbose_name='Názov', max_length=30)
    unit_code = models.CharField(verbose_name='Jednotka', max_length=3)

    panels = [
        FieldPanel('name'),
        FieldPanel('unit_code'),
    ]
