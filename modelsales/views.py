from rest_framework import viewsets

from modelsales.filters import NetworkElementFilter
from modelsales.models import NetworkElement
from modelsales.permissions import IsActiveEmployeePermission
from modelsales.serliazers import ModelsalesSerializer


class ModelsalesViewSet(viewsets.ModelViewSet):
    serializer_class = ModelsalesSerializer
    queryset = NetworkElement.objects.all()
    filterset_clas = NetworkElementFilter
    permission_classes = [IsActiveEmployeePermission]
