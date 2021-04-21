from rest_framework import serializers
from rest_framework.fields import Field
from operator import itemgetter
from .models import Gallery, GalleryImage
import json
import re


class ImageSerializedField(Field):

    def to_representation(self, value):



class GalleryImageSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()
    preview_url = serializers.SerializerMethodField()
    # name = SizeSerializer()

    class Meta:
        model = GalleryImage
        fields = ('url', 'preview_url')

    def get_preview_url(self, image):
        return image.image.get_rendition('width-300').url

    def get_url(self, image):
        return image.image.url


class GallerySerializer(serializers.ModelSerializer):

    images = GalleryImageSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ('images', )
