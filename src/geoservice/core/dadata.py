from dadata import Dadata
from django.conf import settings

DadataAPI = Dadata(settings.TOKEN_DADATA, settings.SECRET_DADATA)
