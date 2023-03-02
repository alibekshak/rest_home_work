from rest_framework.viewsets import ModelViewSet
from .models import Artist, Painting
from .serializers import PaintingSerializer, GetPaintingSerializer, ArtistSerializer


class ArtistModelViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class PaintingModelViewsSet(ModelViewSet):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

    def get_serializer_class(self):
        if self.request.method in ("GET", "HEAD", "OPTIONS"):
            return GetPaintingSerializer

        return PaintingSerializer
