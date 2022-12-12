from rest_framework import serializers

from geoservice.apps.city.models import City


class GeolocationSerializer(serializers.ModelSerializer):
    """Класс сериализации модели City"""

    class Meta:
        model = City
        fields = (
            "address",
            "postal_code",
            "country",
            "federal_district",
            "region_type",
            "region",
            "area_type",
            "area",
            "city_type",
            "city",
            "settlement_type",
            "settlement",
            "lоcation",
        )
