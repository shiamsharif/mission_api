from rest_framework.viewsets import ModelViewSet

from Mission.models import Mission
from Mission.serializers import MissionSerializer


class MissionViewSet(ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()
    