from rest_framework import serializers
from operator import itemgetter
from .models import Pizza, Ingredient, PizzaSize, Size, Menu, MenuItem
import json
import re


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('name', )


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name', )


class PizzaSizeSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    # name = SizeSerializer()

    class Meta:
        model = PizzaSize
        fields = ('name', 'weight', 'price')

    def get_name(self, size):
        return size.name.name


class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True)
    allergens = serializers.SerializerMethodField()
    size_values = PizzaSizeSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ('number', 'name', 'ingredients', 'size_values', 'allergens')

    def get_allergens(self, pizza):
        allergens = []
        for ingredient in pizza.ingredients.all():
            for allergen in ingredient.allergens.all():
                if not re.search('"number": ' + str(allergen.number), json.dumps(allergens), re.M):
                    allergens.append({
                        'number': allergen.number,
                        'name': allergen.name,
                    })

        allergens.sort(key=itemgetter('number'))
        return allergens


class MenuItemSerializer(serializers.ModelSerializer):

    capacity = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ('name', 'description', 'capacity', 'price')

    def get_capacity(self, item):
        return str(item.capacity) + item.capacity_unit.unit_code


class MenuSerializer(serializers.ModelSerializer):

    menu_item = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = ('name', 'menu_item')
