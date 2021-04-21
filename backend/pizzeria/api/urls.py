from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .apps.menu.views import PizzaViewSet, IngredientViewSet, OfferViewSet, Menu
from .apps.gallery.views import GalleryViewSet


router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet)
router.register('ingredient', IngredientViewSet)
# router.register('offer', OfferViewSet)
router.register('menu', Menu, basename='menu')
router.register('gallery', GalleryViewSet, basename='gallery')

urlpatterns = [
    path('', include(router.urls)),
]
