from django.shortcuts import render
from rest_framework import viewsets
from events.models import Event
from events.serializers import EventSerializer

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer