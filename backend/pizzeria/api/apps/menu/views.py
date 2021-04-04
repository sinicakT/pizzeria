from rest_framework import viewsets
from rest_framework.response import Response

from .models import Pizza, Ingredient, Offer
from .serializers import PizzaSerializer, IngredientsSerializer, OfferSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    http_method_names = ['get']


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    http_method_names = ['get']


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    http_method_names = ['get']


class Menu(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
        menu = {
            'pizza': self.extract_pizza(),
            'offer': self.extract_offer(),
            'ingredients_list': self.get_ingredients_list()
        }

        return Response(menu)

    def extract_pizza(self):
        pizzas = Pizza.objects.all()
        return PizzaSerializer(pizzas, many=True).data

    def extract_offer(self):
        offer = Offer.objects.all()
        return OfferSerializer(offer, many=True).data

    def get_ingredients_list(self):
        ingredients = Ingredient.objects.all()
        return IngredientsSerializer(ingredients, many=True).data
