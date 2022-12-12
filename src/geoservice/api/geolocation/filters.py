import django_filters
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

from geoservice.apps.city.models import City
from geoservice.core.dadata import DadataAPI


class GeolocationFilter(django_filters.FilterSet):
    """Фильтр городов в диаметре."""

    address = django_filters.CharFilter(method="address_filter")
    diametr = django_filters.NumberFilter(method="distance_filter")
    location = None

    def address_filter(self, request, *args, **kwargs):
        """Фильтр городов, которые находятся в диаметре 10 километров."""
        if request:
            self.location = DadataAPI.clean("address", self.data.get("address"))
            qs = City.objects.filter(
                lоcation__distance_lte=(
                    Point(
                        float(self.location.get("geo_lon")),
                        float(self.location.get("geo_lat")),
                    ),
                    D(km=10),
                )
            )
        return qs

    def distance_filter(self, request, *args, **kwargs):
        """Фильтр городов, которые находятся в диаметре,
        который мы передаем в запросе.
        """
        if request:
            qs = City.objects.filter(
                lоcation__distance_lte=(
                    Point(
                        float(self.location.get("geo_lon")),
                        float(self.location.get("geo_lat")),
                    ),
                    D(km=self.data.get("diametr")),
                )
            )
        return qs
