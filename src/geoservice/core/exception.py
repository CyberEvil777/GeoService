from rest_framework.exceptions import APIException


class NotFoundCityException(APIException):
    status_code = 404
    default_detail = 'Необходимо отправить адрес!!!'
    default_code = 'service_unavailable'
