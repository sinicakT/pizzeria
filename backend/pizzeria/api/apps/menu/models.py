from django.db import models
from modelcluster.models import ClusterableModel
from django.db.models import Max

from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel


class Ingredient(models.Model):

    class Meta:
        verbose_name = 'Surovina'
        verbose_name_plural = 'Suroviny'
        ordering = ('name',)

    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    allergens = models.ManyToManyField('Allergen', related_name='ingredients')
    price_extra = models.DecimalField(max_digits=4, decimal_places=2)

    panels = [
        FieldPanel('name'),
        FieldPanel('price_extra'),
        FieldPanel('allergens'),
    ]

class Allergen(models.Model):

    def get_next_number():
        allRecords = Allergen.objects.all()
        if len(allRecords) < 1:
            return 1
        new_number_default = allRecords.aggregate(Max('number'))['number__max']+1
        return int(new_number_default)


    number = models.IntegerField(unique=True, default=get_next_number)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return str(self.number) + '. ' + self.name


class PizzaSize(Orderable):

    pizza = ParentalKey('menu.Pizza', related_name='size_values', blank=True, default=None)
    name = models.ForeignKey('crud.Size', verbose_name='Veľkosť', related_name='size', on_delete=models.SET_NULL, null=True)
    weight = models.IntegerField(verbose_name='Hmotnosť')
    price = models.DecimalField(verbose_name='Cena', max_digits=4, decimal_places=2)

    panels = [
        FieldPanel('name'),
        FieldPanel('weight'),
        FieldPanel('price'),
    ]


class Pizza(ClusterableModel):

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizze'
        # ordering = ['number']

    def get_next_number():
        allRecords = Pizza.objects.all()
        if len(allRecords) < 1:
            return 1
        new_number_default = allRecords.aggregate(Max('number'))['number__max']+1
        return int(new_number_default)

    # number = models.IntegerField(verbose_name='Poradové číslo', unique=True, default=get_next_number)
    number = models.IntegerField(verbose_name='Poradové číslo', unique=True, default=get_next_number)
    ingredients = models.ManyToManyField('Ingredient', related_name='pizzas')
    name = models.CharField(verbose_name='Názov', max_length=30, default=None)

    def __str__(self):
        return str(self.number) + '. ' + self.name

    panels = [
        FieldPanel('number'),
        FieldPanel('name'),
        FieldPanel('ingredients'),
        InlinePanel('size_values', label="Varianty")
    ]
    #     # FieldPanel('small_price'),
    #     # FieldPanel('small_weight'),
    #     # FieldPanel('big_price'),
    #     # FieldPanel('big_weight'),
    #     # InlinePanel('ingredients', label='Suroviny'),
    #     # InlinePanel('size_values', label='Hmotnosti'),


class OfferItem(Orderable):

    def __str__(self):
        return self.name

    offer = ParentalKey('menu.Offer', related_name='offer_item', blank=True, default=None)
    name = models.CharField(verbose_name='Názov', max_length=30)
    description = models.CharField(verbose_name='Popis', max_length=255, blank=True)
    capacity = models.FloatField(verbose_name='Hmotnosť')
    capacity_unit = models.ForeignKey('crud.Unit', verbose_name='Jednotka', related_name='unit', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(verbose_name='Cena', max_digits=4, decimal_places=2)


class Offer(ClusterableModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    name = models.CharField(verbose_name='Názov', max_length=30)

    panels = [
        FieldPanel('name'),
        InlinePanel('offer_item', label="Ponuka")
    ]

