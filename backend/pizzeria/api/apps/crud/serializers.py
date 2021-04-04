from rest_framework import serializers
from operator import itemgetter

from .models import Size, Unit

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('name', )


