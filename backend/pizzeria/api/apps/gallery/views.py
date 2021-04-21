from rest_framework import viewsets
from rest_framework.response import Response

from .models import Gallery, GalleryImage
from .serializers import GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    http_method_names = ['get']
