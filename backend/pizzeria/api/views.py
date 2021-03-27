from rest_framework import viewsets
from rest_framework.response import Response

from .models import Pizza, Ingredient, Menu
from .serializers import PizzaSerializer, IngredientsSerializer, MenuSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    http_method_names = ['get']


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    http_method_names = ['get']


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = ['get']


class Offer(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
        offer = {
            'pizza': self.extract_pizza(),
            'menu': self.extract_menu()
        }

        return Response(offer)

    def extract_pizza(self):
        pizzas = Pizza.objects.all()
        return PizzaSerializer(pizzas, many=True).data

    def extract_menu(self):
        menu = Menu.objects.all()
        return MenuSerializer(menu, many=True).data
