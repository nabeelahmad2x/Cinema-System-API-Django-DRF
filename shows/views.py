from rest_framework import viewsets
from .models import Shows
from .serializers import ShowsSerializer


class ShowsViewSet(viewsets.ModelViewSet):
    queryset = Shows.objects.all()
    serializer_class = ShowsSerializer
