from rest_framework import viewsets
from .models import Emissions
from .serializers import EmissionsSerializer

class EmissionsViewSet(viewsets.ModelViewSet):
    queryset = Emissions.objects.all()
    serializer_class = EmissionsSerializer