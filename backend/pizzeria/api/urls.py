from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PizzaViewSet, IngredientViewSet, MenuViewSet


router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet)
router.register('ingredient', IngredientViewSet)
router.register('menu', MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]