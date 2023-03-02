from rest_framework.routers import DefaultRouter
from .views import ArtistModelViewSet, PaintingModelViewsSet

router = DefaultRouter()

router.register('artist', ArtistModelViewSet)
router.register('painting', PaintingModelViewsSet)

urlpatterns = router.urls
