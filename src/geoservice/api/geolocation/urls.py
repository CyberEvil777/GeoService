from django.urls import path

from geoservice.api.geolocation.views import GeolocationView

urlpatterns = [
    path("geolocation/", GeolocationView.as_view(), name="geolocation"),
]
