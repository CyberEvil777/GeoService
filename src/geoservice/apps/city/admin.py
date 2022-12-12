from django.contrib import admin
from django.contrib.auth.models import Group, User

from geoservice.apps.city.models import City

# Register your models here.
admin.site.register(City)
admin.site.unregister(User)
admin.site.unregister(Group)
