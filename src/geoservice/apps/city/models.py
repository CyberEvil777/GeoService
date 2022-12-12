from django.contrib.gis.db import models


class City(models.Model):
    """Модель для данных с .csv файла"""

    address = models.CharField(verbose_name="Адрес", max_length=255)
    postal_code = models.PositiveIntegerField(verbose_name="Почтовый индекс")
    country = models.CharField(verbose_name="Страна", max_length=100)
    federal_district = models.CharField(
        verbose_name="Федеральный район", max_length=100
    )
    region_type = models.CharField(verbose_name="Тип региона", max_length=20)
    region = models.CharField(verbose_name="Региона", max_length=100)
    area_type = models.CharField(verbose_name="Тип области", max_length=10, null=True)
    area = models.CharField(verbose_name="Область", max_length=100, null=True)
    city_type = models.CharField(verbose_name="Тип города", max_length=100)
    city = models.CharField(verbose_name="Город", max_length=100)
    settlement_type = models.CharField(verbose_name="Тип поселка", max_length=100)
    settlement = models.CharField(verbose_name="Поселок", max_length=100)
    lоcation = models.PointField(
        verbose_name="Геопозиция",
        geography=True,
        help_text="Первым значением идет долгота longitude, а вторым значением широта latitude",
    )

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
