from rest_framework import serializers
from operator import itemgetter
from .models import Pizza, Ingredient, Allergen, PizzaSize, Size
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

    name = SizeSerializer()

    class Meta:
        model = PizzaSize
        fields = ('name', 'weight', 'price')



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
