from django_filters import rest_framework as filters

from modelsales.models import NetworkElement


class NetworkElementFilter(filters.FilterSet):
    class Meta:
        model = NetworkElement
        fields = {
            'country': ['exact'],
        }