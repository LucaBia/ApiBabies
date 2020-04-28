from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory

from babies.models import Baby
from events.models import Event

from babies.serializers import BabySerializer
from events.serializers import EventSerializer


# Create your views here.
class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    # Permisos
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'babies.view_baby',
                    'destroy': False,
                    'update': 'babies.change_baby',
                    'partial_update': 'babies.change_baby',
                    # 'notify': evaluar_notify,
                    'events': 'babies.view_baby'
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.view_baby', user, baby)
        assign_perm('babies.change_baby', user, baby)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        allEvents=[]
        for event in Event.objects.filter(baby=baby):
            allEvents.append(EventSerializer(event).data)
        return Response(allEvents)