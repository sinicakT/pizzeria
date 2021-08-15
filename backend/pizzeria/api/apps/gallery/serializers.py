from rest_framework import serializers
from .models import Gallery, GalleryImage
from wagtail.images.views.serve import generate_image_url

#
#
# class ImageSerializedField(Field):
#
#     def to_representation(self, value):


class GalleryImageSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()
    preview_url = serializers.SerializerMethodField()
    # name = SizeSerializer()

    class Meta:
        model = GalleryImage
        fields = ('url', 'preview_url')

    def get_preview_url(self, obj):
        return generate_image_url(obj.image, 'width-300')

    def get_url(self, obj):
        width = 'width-' + str(obj.image.width)
        return generate_image_url(obj.image, width)


class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ('name', 'images')