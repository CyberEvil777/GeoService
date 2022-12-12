import csv
from itertools import islice

from django.conf import settings
from django.contrib.gis.geos import Point
from django.db import transaction

from geoservice.apps.city.models import City


def parse_city():
    with open(settings.PATH_CITY_CSV, newline="") as csvfile:
        city_csv = csv.DictReader(csvfile)
        batch_size = 100
        city = (
            City(
                address=row.get("address"),
                postal_code=int(row.get("postal_code") or "0"),
                country=row.get("country"),
                federal_district=row.get("federal_district"),
                region_type=row.get("region_type"),
                region=row.get("region"),
                area_type=row.get("area_type"),
                area=row.get("area"),
                city_type=row.get("city_type"),
                city=row.get("city"),
                settlement_type=row.get("settlement_type"),
                settlement=row.get("settlement"),
                lоcation=Point(float(row.get("geo_lon")), float(row.get("geo_lat"))),
            )
            for row in city_csv
        )
        with transaction.atomic():
            while True:
                batch = list(islice(city, batch_size))
                if not batch:
                    break
                City.objects.bulk_create(batch, batch_size)
