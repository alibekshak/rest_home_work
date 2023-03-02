from rest_framework import serializers
from .models import Artist, Painting


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'full_name', 'slug')


class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ('id', 'paint', 'category', 'image', 'text', 'created_at')


class GetPaintingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Painting
        fields = ('id', 'paint', 'category', 'image', 'text', 'created_at')
