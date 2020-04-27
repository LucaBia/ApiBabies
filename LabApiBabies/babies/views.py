from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from babies.models import Baby
from events.models import Event

from babies.serializers import BabySerializer
from events.serializers import EventSerializer


# Create your views here.
class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    
@action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        allEvents=[]
        for event in Event.objects.filter(baby=baby):
            allEvents.append(EventSerializer(event).data)
        return Response(allEvents)