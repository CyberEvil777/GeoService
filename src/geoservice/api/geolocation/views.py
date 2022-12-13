from django_filters.rest_framework import DjangoFilterBackend
from geoservice.api.geolocation.filters import GeolocationFilter
from geoservice.api.geolocation.serializers import GeolocationSerializer
from geoservice.apps.city.models import City
from rest_framework import generics


class GeolocationView(generics.ListAPIView):
    """View для поиска по НП."""

    queryset = City.objects.all()
    serializer_class = GeolocationSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_class = GeolocationFilter
