import django_filters

from .models import *

class RentFilter(django_filters.FilterSet):
    class Meta:
        model = Rent
        fields = ['location']